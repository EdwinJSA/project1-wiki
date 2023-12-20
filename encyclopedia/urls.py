from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("WIKI/<str:entry>", views.entry_page, name="entry"),
    path("createpage", views.createEntry, name="createpage"),
    path("edit_Entry/<str:entry>", views.editEntry, name="edit_Entry"),
    path("search", views.search, name="search"),
    path("random_page", views.random_page, name="random_page"),
]
