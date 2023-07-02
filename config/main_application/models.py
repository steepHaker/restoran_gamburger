from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
    name = models.CharField('Названиие категории', max_length=255, default="")
    image = models.ImageField('Иконка', upload_to='category_images/')
    slug = models.SlugField()
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    # class MPTTMeta:
    #     order_insertion_by = ['name']
    

    def __str__(self):
        return self.name
    
class UpperSlider(models.Model):
    image = models.ImageField("верхний слайдер", upload_to='slider_images/')
    description = models.TextField("описание слайдера", unique=True, default="")
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description
    
class Dish(models.Model):
    name = models.CharField('Названиие блюда', max_length=255)
    description = models.TextField('Описание блюда, состав', max_length=500)
    CURRENCY_CHOICES = (
        ('₽', 'RUB'),
        ('$', 'USD'),
        ('€', 'EUR'),
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Фото блюда', upload_to='dishs/', default="")
    currency = models.CharField('Валюта', max_length=3, choices=CURRENCY_CHOICES, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class DishTitle(models.Model):
    title = models.CharField('Описание категории меню',max_length=1000, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Menu(models.Model):
#     name = models.CharField('Имя категории', max_length=50)
#     image = models.ImageField('Иконка', upload_to='menu_icon')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
