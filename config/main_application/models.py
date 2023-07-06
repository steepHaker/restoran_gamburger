from audioop import reverse
from django.db import models
from django.shortcuts import render
from django.urls import reverse


def generate_page_urls():
    pages = Page.objects.all()
    page_urls = {}
    for page in pages:
        url = reverse('menu_detail', kwargs={'menu_slug': page.slug})
        page_urls[page.namePage] = url
    return page_urls

class Page(models.Model):
    namePage = models.CharField('Название страницы', max_length=100, default="")
    slug = models.CharField("Отображение в браузере", max_length=200, unique=True, default="")

    def menu_view(request):
        page_urls = generate_page_urls()
        return render(request, 'menu.html', {'page_urls': page_urls})

    def __str__(self):
        return self.namePage

class Category(models.Model):
    name = models.CharField('Название категории', max_length=255, default="")
    image = models.ImageField('Иконка', upload_to='category_images/')
    slug = models.SlugField(default="")


    def __str__(self):
        return self.name
    
class Dish(models.Model):
    name = models.CharField('Название блюда', max_length=255, default="")
    description = models.TextField('Описание блюда, состав', max_length=500, default="")
    CURRENCY_CHOICES = (
        ('₽', 'RUB'),
        ('$', 'USD'),
        ('€', 'EUR'),
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Фото блюда', upload_to='dishs/', default="")
    currency = models.CharField('Валюта', max_length=3, choices=CURRENCY_CHOICES, default="Rub")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    related_Page = models.ForeignKey(Page, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name

class Logo(models.Model):
    title = models.CharField('Название сайта', max_length=255, default="")
    iconMenu = models.ImageField(upload_to='icon', default="")

    def __str__(self):
        return self.title
    
class UpperSlider(models.Model):
    image = models.ImageField("верхний слайдер", upload_to='slider_images/')
    description = models.TextField("описание слайдера", unique=True, default="")
    title = models.CharField('Текст меню', max_length=1000, default="")
    related_Page = models.ForeignKey(Page, on_delete=models.CASCADE, to_field='slug', default="", related_name='upper_sliders')

    def __str__(self):
        return self.title
    
class InfoBanner(models.Model):
    title = models.CharField(max_length=300, blank=True, default="your title")
    text = models.TextField(blank=True, default="your text")
    image = models.ImageField(blank=True, upload_to="InfoBanner")
    image1 = models.ImageField(blank=True, upload_to="InfoBanner")
    page = models.ForeignKey(Page, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
    
    
    