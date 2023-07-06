from django.contrib import admin

from blog import models
from blog.models import Post, Category

admin.site.register(models.Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'create_at')
    save_as = True
    save_on_top = True

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'  # Сокращение текста до 20 символов
        else:
            return obj.title

    short_title.short_description = 'Title'  # Краткое описание поля

admin.site.register(Post, PostAdmin)
admin.site.register(models.Category)
