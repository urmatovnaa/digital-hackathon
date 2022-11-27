from django.db import models
from event_app.models import Speaker, Category


class Course(models.Model):
    """Info about speakers"""
    TIME_STUDY_CHOICES = (('оффлайн', 'оффлайн'), ('онлайн', 'онлайн'),)
    CERTIFICATE_CHOICES = (('есть', 'есть'), ('нет', 'нет'),)
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    photo = models.ImageField(upload_to='course_photo', verbose_name='Фото')
    time_study = models.CharField(verbose_name='Формат обучения', choices=TIME_STUDY_CHOICES, default=1,
                              max_length=255, blank=False)
    duration = models.CharField(verbose_name='Продолжительность курса', max_length=255)
    certificate = models.CharField(verbose_name='Сертификат по окончании',
                                   choices=CERTIFICATE_CHOICES, default=1,
                                   max_length=255, blank=False)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    overview = models.TextField(verbose_name='Описание курса')
    contributors = models.ForeignKey(Speaker, verbose_name='Преподаватели', on_delete=models.CASCADE,
                                     null=True, blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name
