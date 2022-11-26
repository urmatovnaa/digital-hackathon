from django.db import models

from account_app.managers import get_default_profile_image


class Question(models.Model):
    """ Questions model """
    owner = models.CharField(max_length=120,
                             verbose_name='Владелец вопроса',
                             null=True)
    profile = models.ImageField(upload_to='avatar',
                                verbose_name='Aватар',
                                default=get_default_profile_image)
    text = models.CharField(max_length=500,
                            verbose_name='Текст')
    data_creating = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Дата')

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"{self.text} - {self.data_creating}"

    def save(self, *args, **kwargs):
        self.owner = 'Сообщение сообщества'
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    """ Answers model """
    owner = models.CharField(max_length=120,
                             null=True,
                             verbose_name='Владелец ответа')
    profile = models.ImageField(upload_to='avatar',
                                verbose_name='Aватар',
                                default=get_default_profile_image)
    text = models.CharField(max_length=500,
                            verbose_name='Текст')
    data_creating = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Дата')
    question = models.ForeignKey(Question,
                                 models.CASCADE,
                                 verbose_name='Вопрос',
                                 related_name='answers')

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.text} - {self.data_creating}"

    def save(self, *args, **kwargs):
        self.owner = 'Сообщение сообщества'
        super(Answer, self).save(*args, **kwargs)
