from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from .form import ContactForm
from .models import Book
from .form import BookForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,logout
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
# Create your views here.



#to show all the books listed in the database
class ListOfBooks(ListView):
    model = Book
    context_object_name = 'books'
    template_name='list_of_books.html'



#to show all the books that are published

class ListOfPublishedBooks(ListView):
    model=Book
    context_object_name='books'
    template_name='published_books.html'


    #using custom book manager in model to fetch only the published books
    def get_queryset(self):
        return Book.objects.get_published_books()


#a  view to show the details of a book
class DetailsOfBook(DetailView,LoginRequiredMixin):
    model=Book
    context_object_name='book'
    template_name='book_detail.html'
    

#to add a new book

class CreateBook(CreateView,LoginRequiredMixin):
    model=Book
    form_class=BookForm
    template_name='bookForm.html'
    success_url=reverse_lazy('list')


#to update a book

class UpdateBook(UpdateView,LoginRequiredMixin):
    model=Book
    form_class=BookForm
    template_name='updateBook.html'
    success_url=reverse_lazy('list')

#to Delete a book

class DeleteBook(DeleteView,LoginRequiredMixin):
    model=Book
    template_name='deleteBook.html'
    success_url=reverse_lazy('list')


class ContactFormView(FormView):
    template_name='contact_form.html'
    form_class=ContactForm
    success_url=reverse_lazy('contact_success')

    def form_valid(self, form)-> HttpResponse:
        return super().form_valid(form)


    
    
