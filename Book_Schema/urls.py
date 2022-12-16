from django.urls import path
from . import views


# route_paths for the database app

urlpatterns = [
    path('add/new/author/', views.addAuthor),
    path('add/new/publisher/', views.addPublisher),
    path('add/new/book/', views.addBook),
    path('get/all/author/', views.getAuthors),
    path('get/all/publisher/', views.getPublishers),
    path('get/all/book/', views.getBooks),
]
