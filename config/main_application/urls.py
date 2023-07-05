from django.shortcuts import redirect
from django.urls import path
from . import views 



urlpatterns = [  
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('home/', views.HomeView.as_view(), name='home'),
]