from django.contrib import admin
from . import models
# from mptt.admin import  MPTTModelAdmin


@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [ "name", "description",  "category", "price", "currency" ]
    save_as = True
    save_on_top = True

admin.site.register(models.Category)
admin.site.register(models.Logo)
admin.site.register(models.UpperSlider)
admin.site.register(models.Page, ) #MPTTModelAdmin
admin.site.register(models.InfoBanner ) 




# @admin.register(models.UpperSlider)
# class SlidervView(admin.ModelAdmin):
#     list_display = ["description"]

# @admin.register(models.Dish)
# class SliderView(admin.ModelAdmin):
#     list_display = ["name", "desption", "price_rub", "price_usd", "price_eur"]

# @admin.register(models.UpperSlider)
# class SlidervView(admin.UpperSlider):
#     list_display = ["description"]
    





    


