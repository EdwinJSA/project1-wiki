from django import forms

class createEntryForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput, max_length=100, required=True)  
    content = forms.CharField(label="Content in Markdown Format", widget=forms.Textarea, required=True)
    
class editEntryForm(forms.Form):
    content = forms.CharField(label="Edit Content in Markdown Format", widget=forms.Textarea, required=True)