from django.urls import path

#importing all the views
from .views import (
    ListOfBooks,ListOfPublishedBooks,DetailsOfBook,CreateBook,UpdateBook,DeleteBook,ContactFormView,BookListView,BookUpdateDestroy,PublisherView,AuthorView
)
from django.shortcuts import render


#defining url paths
urlpatterns = [
    path('list/',ListOfBooks.as_view(),name='list'),
    path('published_books/',ListOfPublishedBooks.as_view(),name='published_list'),
    path('book_details/<int:pk>/',DetailsOfBook.as_view(),name='book_details'),
    path('add_book/',CreateBook.as_view(),name='add_book'),
    path('update/<int:pk>',UpdateBook.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteBook.as_view(),name='delete'),
    path('contact/add',ContactFormView.as_view()),
    path('contact_success/',lambda request:render (request,'success/contact_success.html'),name='contact_success'),

    #api end points
    path('api/books/list',BookListView.as_view(),name='book_list'),
    path('api/books/update_destroy/<int:pk>',BookUpdateDestroy.as_view(),name='update_destroy'),
    path('api/publisher/<int:pk>',PublisherView.as_view(),name="publisher"),
    path('api/publisher',PublisherView.as_view(),name="publisher"),
    path('api/author',AuthorView.as_view(),name='author'),
    path('api/author/<int:pk>',AuthorView.as_view(),name='author'),
    
    
]
