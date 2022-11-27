from django.db import models
from datetime import datetime
from event_app.models import Category
from main.settings import AUTH_USER_MODEL


class Article(models.Model):
    """Info about article"""
    name = models.CharField(verbose_name='Название', max_length=255)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    photo = models.ImageField(upload_to='article_photo', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name
