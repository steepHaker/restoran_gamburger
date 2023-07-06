from django.views.generic import ListView
from .models import Dish, InfoBanner, UpperSlider, Category, Page, Logo

class BaseView(ListView):
    model = Dish
    template_name = 'base.html'
    page_slug = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upper_slider'] = UpperSlider.objects.get(related_Page__slug='home')
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
        try:
            current_page = Page.objects.get(slug='home')
            context['upper_slider'] = UpperSlider.objects.get(related_Page=current_page)
        except (Page.DoesNotExist, UpperSlider.DoesNotExist):
            context['upper_slider'] = None
        return context
    
class MenuView(BaseView):
    template_name = 'main/page_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            current_page = Page.objects.get(slug='menu')
            context['upper_slider'] = UpperSlider.objects.get(related_Page=current_page)
        except (Page.DoesNotExist, UpperSlider.DoesNotExist):
            context['upper_slider'] = None
        return context
    

