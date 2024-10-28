from django.urls import path
from .views import UserLoginView,UserRegistrationView,CustomLogoutView  #importing all the  views


#defining the url path
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
]
