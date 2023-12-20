from django.shortcuts import render
from markdown import markdown   
from django.utils.safestring import mark_safe
from .forms import createEntryForm, editEntryForm
from . import util
from .models import entryModel
from django.contrib import messages
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry):
    return render(request, "encyclopedia/entry.html/", {
        "entry": entry, 
        "content_entries": mark_safe(markdown(util.get_entry(entry))),
    })
    
def createEntry(request):
    if request.method == 'POST':
        entry = request.POST['title']
        if entry not in util.list_entries():
            util.save_entry(request.POST['title'], request.POST['content'])
            entryModel.objects.create(title=request.POST['title'], content=request.POST['content'])
            return entry_page(request, entry)
        else: 
            messages.error(request, 'Entry already exists!')
            return render(request, "encyclopedia/newEntry.html", {
            "form": createEntryForm()
            })
    else:
        return render(request, "encyclopedia/newEntry.html", {
            "form": createEntryForm()
        })
        
def editEntry(request, entry):
    if request.method == 'POST':
        util.save_entry(entry, request.POST['content'])
        return entry_page(request, entry)
    else:
        content = util.get_entry(entry)
        return render(request, "encyclopedia/editEntry.html", {
            "form" : editEntryForm(initial={'content': content}),
        })
    
def wordInList(word, list):
    matched = [element for element in list if word.lower() in element.lower()]
    return matched
    
def search(request):
    if request.method == 'POST':
        word = request.POST['q']
        list_entries = util.list_entries()
        # print(word)
        # print(list_entries)
        # print(wordInList(word,list_entries))
        if len(wordInList(word,list_entries)) == 0:
            return nofound(request)
        
        if wordInList(word,list_entries)[0] == word:
            return entry_page(request, wordInList(word,list_entries)[0])
            
        return render(request, "encyclopedia/search.html", {
            "entries": wordInList(word,list_entries)
        })
        
def random_page(request):
    list_entries = util.list_entries()
    return entry_page(request, list_entries[random.randint(0, len(list_entries)-1)])

def nofound(request):
    return render(request, "encyclopedia/404.html")