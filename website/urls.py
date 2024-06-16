from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index page'),
    path('login/',login,name='login page'),
    path('register/',register,name='register page'),
    path('Home/',home,name='home page'),
    path('menu/',menu,name='menu'),
    path('final/',final,name='cart')
]