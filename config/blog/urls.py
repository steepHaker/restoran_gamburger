from django.urls import path
from .views import BlogView, SinglePostView

urlpatterns = [
    path('home/blog/', BlogView.as_view(), name='blog'),
    path('home/blog/<slug:post_slug>/', SinglePostView.as_view(), name='single_blog'),
]
