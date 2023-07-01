from django.shortcuts import render
from django.views.generic import ListView
from .models import Dish, UpperSlider, Category


class MenuView(ListView):
    model = Dish
    template_name = 'menu/menu_list.html'
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return Dish.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upper_slider'] = UpperSlider.objects.first()
        context['category_name'] = Category.objects.all()
        context['category_dish'] = Category.objects.prefetch_related('dish_set').all()
        context['dish_desc'] = Dish.objects.first
        return context
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category_slug = self.kwargs.get('slug')
    #     title = self.kwargs.get('title')
    #     context['upper_slider'] = UpperSlider.objects.first()
    #     context['category_name'] = Category.objects.get(slug=category_slug)
    #     context['category_dish'] = Category.objects.prefetch_related('dish_set').all()
    #     context['dish_desc'] = Dish.objects.filter(title=title).first()
    #     return context




class HomeView(ListView):
    model = Dish
    paginate_by = 9
    template_name = "base.html"







