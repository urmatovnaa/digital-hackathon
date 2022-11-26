from django.db import models
from datetime import datetime
from account_app.models import Account


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


class Speaker(models.Model):
    """Info about speakers"""
    fullname = models.CharField(verbose_name="ФИО", max_length=255)
    position = models.CharField(verbose_name="Должность", max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=150)

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"

    def clean(self):
        self.fullname = self.fullname.capitalize()

    def __str__(self):
        return self.fullname


class Event(models.Model):
    """Information about Events"""
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    data = datetime.now()
    photo = models.ImageField(upload_to='event_photo')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True, blank=True)
    time = models.CharField(verbose_name='Время', max_length=255)
    description = models.TextField(verbose_name="Чему вы научитесь?")
    about = models.TextField(verbose_name="О программе")
    speakers_detail = models.ManyToManyField(Speaker, verbose_name='Спикеры', blank=True, related_name='speakers_detail')
    user = models.ForeignKey(Account, verbose_name='Владелец', on_delete=models.CASCADE)
    number_for_seats = models.IntegerField(verbose_name='Количество мест')

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Registered(models.Model):
    """Registered"""
    event = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.SET_NULL,
                              related_name='people_count', null=True, blank=True)
    user = models.ForeignKey(Account, verbose_name='Участник', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return f'{self.event}'

