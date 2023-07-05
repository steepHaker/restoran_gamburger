from multiprocessing import context
from pickle import NONE
from urllib import request
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Dish, InfoBanner, UpperSlider, Category, Page, Logo

class BaseView(ListView):
    model = Dish
    template_name = NONE
    page_slug = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['upper_slider'] = UpperSlider.objects.get(related_Page__slug=self.page_slug)
        except UpperSlider.DoesNotExist:
            context['upper_slider'] = None

        context['category_name'] = Category.objects.all()
        context['category_dish'] = Category.objects.prefetch_related('dish_set').all()
        context['pages'] = Page.objects.all()
        context['icons'] = Logo.objects.all()
        
        return context





class HomeView(BaseView):
    template_name = 'main/homeMain.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = InfoBanner.objects.all()
        return context
    

class MenuView(BaseView):
    template_name = 'main/menu.html'

    
   
    




