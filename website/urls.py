from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('',index,name='index page'),
    path('login/',login,name='login page'),
    path('register/',register,name='register page'),
    path('Home/',home,name='home page'),
    path('menu/',menu,name='menu'),
    path('final/',final,name='cart'),
    path('logout/',logout,name='logout'),
    path('orders/',Orders.as_view(),name='orders'),
    path('Uname/',get_Uname,name='Uname')
]