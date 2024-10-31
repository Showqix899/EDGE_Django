#django
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views import View
from django.contrib.auth import logout

#rest_framework





# Create your views here.

#user login 
class UserLoginView(LoginView):
    template_name='login.html'
    success_url=reverse_lazy('list')


#user register
class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

#user  logout
class CustomLogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('list')