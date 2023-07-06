from django.urls import path
from main_application import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/menu/', views.MenuView.as_view(), name='menu'),
]
