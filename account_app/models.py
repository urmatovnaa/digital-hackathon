from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from account_app.managers import MyAccountManager, get_default_profile_image


class Account(AbstractUser):
    """ My user model """

    first_name = None
    last_name = None
    username = None

    fullname = models.CharField(max_length=100,
                                verbose_name='ФИО')
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100,
                                verbose_name='Должность')
    organisation = models.CharField(max_length=100,
                                    verbose_name='Организация')
    profile_image = models.ImageField(upload_to='avatar',
                                      null=True, blank=True,
                                      default=get_default_profile_image,
                                      verbose_name='Аватар')

    date_joined = models.DateField(verbose_name='Дата регистрации',
                                   default=timezone.now)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def clean(self):
        self.fullname = self.fullname.capitalize()

    def __str__(self):
        return f'{self.fullname}'

