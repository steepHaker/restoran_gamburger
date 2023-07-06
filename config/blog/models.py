from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
    
class Tag(models.Model):
    name = models.CharField(max_length=50, default="")
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, default="")
    
    def __str__(self):
        return self.name

class Post(models.Model):
    sliderText = models.CharField(max_length=500, default="")
    title = models.CharField(max_length=300, default="")
    images = models.ImageField(upload_to='blog')
    text = RichTextField(default="")
    miniText = models.TextField( max_length=1000, default="")
    text_2 = RichTextField(default="")
    create_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="Post")
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    slug = models.SlugField(max_length=100, default="")

    def get_absolute_url(self):
        return reverse('single_blog', kwargs={'post_slug': self.slug})
  

    def __str__(self):
        return self.title
    

    








