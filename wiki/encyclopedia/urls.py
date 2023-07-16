from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("title/", views.title, name="title"),
    path("newPage/", views.newPage, name="newPage"),
    path("newEntry/", views.newEntry, name="newEntry"),
    path("<query>/editPage", views.editPage, name="editPage"),
    path("<query>/Link", views.titleLink, name='Link'),
    path("randomPage", views.randomPage, name="randomPage" ) 
]
