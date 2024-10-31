
######django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView

from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,logout
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

### models

from .models import Book,Author,Publisher
 
#form
from .form import ContactForm
from .form import BookForm


#########rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin,CreateModelMixin
from rest_framework import permissions


#########serializers

from .serializers import BookSerializer,PublisherSerializer,AuthorSerializer

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
    


#APIS

# to get all the books and post  a new book (model Book)


class BookListView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        book=request.data
        serializer=BookSerializer(data=book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#for update  and delete (model Book)

class BookUpdateDestroy(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    http_method_names=('get','put','post','delete')

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
    
    def  delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    


#for Publisher 
class PublisherView(APIView):

    #to get all the publisher
    def get(self,request,pk=None):

        #for single publisher
        if  pk is not None:
            publisher=Publisher.objects.get(id=pk)
            serializer=PublisherSerializer(publisher)
            return Response(serializer.data)
        #all the publisher
        publishers=Publisher.objects.all()
        serializer=PublisherSerializer(publishers,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #to post new publisher
    def  post(self,request):
        publisher=request.data
        serializer=PublisherSerializer(data=publisher)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #to update   publisher

    def put(self,request,pk):
        publisher=get_object_or_404(Publisher,pk=pk)
        serializer=PublisherSerializer(publisher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #to delete  publisher

    def delete(self,request,pk):
        publisher=get_object_or_404(Publisher,pk=pk)
        publisher.delete()
        return Response({'msg':'publisher deleted'})

    #to partialy update  publisher

    def patch(self,request,pk):
        publisher=get_object_or_404(Publisher,pk=pk)
        serializer=PublisherSerializer(publisher,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class AuthorView(APIView):

    #to get all the publisher
    def get(self,request,pk=None):

        #for single publisher
        if  pk is not None:
            author=Author.objects.get(id=pk)
            serializer=AuthorSerializer(author)
            return Response(serializer.data)
        #all the publisher
        authors=Author.objects.all()
        serializer=AuthorSerializer(authors,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #to post new publisher
    def  post(self,request):
        author=request.data
        serializer=AuthorSerializer(data=author)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #to update   publisher

    def put(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        serializer=AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #to delete  publisher

    def delete(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        author.delete()
        return Response({'msg':'Author deleted'})

    #to partialy update  publisher

    def patch(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        serializer=AuthorSerializer(author,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    






