from django.shortcuts import redirect
from django.urls import path
from . import views 



urlpatterns = [  
    path('', views.HomeMyView.as_view(), name='home'),
    # Добавьте следующую строку для перенаправления /home/ на homeMain.html
    #path('home/', views.HomeMyView.as_view(), name=''),
    path('<slug:slug>/', views.HomeMyView.as_view(), name="home-main"),
    # path('', views.HomeMyView.as_view(), name='main/homeMain.html'),
    # path('', views.MenuView.as_view(), name='menu'),
    # path('menu/<slug:slugPage>/', views.MenuView.as_view(), name='menu'),
    # path('pages/', views.PageView.as_view(), name='page'),
]