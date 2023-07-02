from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Dish, UpperSlider, Category, DishTitle

def menu_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    context = {
        'category_name': category,
        'dish_titles': category.dishtitle_set.all(),
        'category_dish': DishTitle.objects.filter(category=category),
    }
    return render(request, 'menu_list.html', context)


class MenuView(ListView):
    model = Dish
    template_name = 'menu/menu_list.html'
    paginate_by = 10

    def get_queryset(self):# ДЛЯ ПЕРЕХОДА НА СТРАНИЦУ
        category_slug = self.kwargs.get('slug')
        return Dish.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upper_slider'] = UpperSlider.objects.first()# НЕ ТРОГАТЬ
        context['category_name'] = Category.objects.all()# НЕ ТРОГАТЬ
        context['category_dish'] = Category.objects.prefetch_related('dish_set').all()# НЕ ТРОГАТЬ
        #context['dish_desc'] = Dish.objects.first
        return context

class HomeView(ListView):
    model = Dish
    paginate_by = 9
    template_name = "base.html"







