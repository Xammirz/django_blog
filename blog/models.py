from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    url = models.SlugField(unique=True, verbose_name='Ссылка')
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')   #Категория
    title = models.CharField(max_length=35)  #Название
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)   #Изображение поста
    small_description = models.TextField(max_length=100)    #Малое описание
    description = models.TextField()    #Описание
    created = models.DateTimeField(auto_now_add=True)   #Время создания продукта
    updated = models.DateTimeField(auto_now=True)   #Время последнего обнавления продутка
    def get_absolute_url(self): # new
        return reverse('news')

    def __str__(self):
        return self.title
