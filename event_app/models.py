from django.db import models
from datetime import datetime


class Category(models.Model):
    """Category for events, courses"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Speakers(models.Model):
    """Info about speakers"""
    fullname = models.CharField(verbose_name="ФИО", max_length=255)
    position = models.CharField(verbose_name="Должность", max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=150)

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Events(models.Model):
    """Information about Events"""
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    data = datetime.now()
    photo = models.ImageField(upload_to='event_photo')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True, blank=True)
    time = models.CharField(verbose_name='Время', max_length=255)
    description = models.TextField(verbose_name="Чему вы научитесь?")
    about = models.TextField(verbose_name="О программе")
    speaker = models.ManyToManyField(Speakers, verbose_name='Спикеры', blank=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

