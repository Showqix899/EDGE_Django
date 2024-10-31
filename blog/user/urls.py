
#django
from django.urls import path

#app
from .views import UserLoginView,UserRegistrationView,CustomLogoutView,LogoutView  #importing all the  views

#rest framework

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#defining the url path
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),

    #api
    path('token', TokenObtainPairView.as_view(),name='token_obtain'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('token/logout',LogoutView.as_view(),name='token_logout'),
    
]
