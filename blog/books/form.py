from django import forms
from .models import Book
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

#creating a form to  add a new book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description', 'author', 'publication_date', 'is_published','publisher','price']  # Define which fields to include in the form


    def  clean_price(self):
            price = self.cleaned_data.get('price')

            if price is None:
                raise forms.ValidationError('Price cannot be empty.')
        
            if price <= 0:
                raise forms.ValidationError('Price must be a positive number.')   

            return price
class ContactForm(forms.Form):

    name=forms.CharField(max_length=200)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)  #textarea is a widget that allows for multiple lines
    #cleaned email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise ValidationError('Please use an email that ends with @example.com.')
        return email




    