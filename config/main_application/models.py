from django.db import models

class Category(models.Model):
    title = models.CharField('Описание категории меню',max_length=1000, default="")
    name = models.CharField('Названиие категории', max_length=255, default="")
    image = models.ImageField('Иконка', upload_to='category_images/')
    slug = models.SlugField()
    

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
        ('RUB', '₽'),
        ('USD', '$'),
        ('EUR', '€'),
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Фото блюда', upload_to='dishs/', default="")
    currency = models.CharField('Валюта', max_length=3, choices=CURRENCY_CHOICES, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




# from django.db import models

# class Category(models.Model):
#     title = models.CharField(max_length=255, default="")
#     name = models.CharField(max_length=255, default="")
#     image = models.ImageField(upload_to='category_images/')
#     slug = models.SlugField()
    

#     def __str__(self):
#         return self.name
    
# class UpperSlider(models.Model):
#     image = models.ImageField(upload_to='slider_images/')
#     description = models.TextField(unique=True, default="")
#     related_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.description



# class DishTitle(models.Model):
#     title = models.CharField(max_length=255, default="")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)#category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title



# class Dish(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(max_length=500)
#     CURRENCY_CHOICES = (
#         ('RUB', '₽'),
#         ('USD', '$'),
#         ('EUR', '€'),
#     )
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='dishs/', default="")
#     currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



