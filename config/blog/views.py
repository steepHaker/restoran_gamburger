
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from blog.models import Post
from main_application.views import BaseView

from main_application.models import Page, UpperSlider



class BlogView(BaseView):
    template_name = 'blogPage/blog.html'
    # model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all() #get(related_Page__slug='home')
        try:
            current_page = Page.objects.get(slug='blog')
            context['upper_slider'] = UpperSlider.objects.get(related_Page=current_page)
        except (Page.DoesNotExist, UpperSlider.DoesNotExist):
            context['upper_slider'] = None
        return context
    
class SinglePostView(DetailView):
    model = Post
    template_name = 'blogPage/single-blog.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            current_page = Page.objects.get(slug='blog')
            context['upper_slider'] = UpperSlider.objects.get(related_Page=current_page)
        except (Page.DoesNotExist, UpperSlider.DoesNotExist):
            context['upper_slider'] = None
        return context

    



