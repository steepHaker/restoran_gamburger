from urllib import request
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Dish, InfoBanner, UpperSlider, Category, Page, Logo


class HomeMyView(ListView):
    model = Dish
    paginate_by = 10
    template_name = "main/homeMain.html"
    page_slug = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upper_slider'] = UpperSlider.objects.get(related_Page__slug=self.page_slug)
        context['category_name'] = Category.objects.all()
        context['category_dish'] = Category.objects.prefetch_related('dish_set').all()
        context['pages'] = Page.objects.all()
        context['icons'] = Logo.objects.all()
        return context

    
class MenuView(HomeMyView):
    template_name = 'main/menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = InfoBanner.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.path == '/home/':
            return redirect('home')

        return super().get(request, *args, **kwargs)


