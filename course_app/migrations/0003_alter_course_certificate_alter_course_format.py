# Generated by Django 4.1.3 on 2022-11-27 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_alter_course_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(choices=[(1, 'есть'), (2, 'нет')], default=1, max_length=255, null=True, verbose_name='Сертификат по окончании'),
        ),
        migrations.AlterField(
            model_name='course',
            name='format',
            field=models.CharField(choices=[(1, 'offline'), (2, 'online')], default=1, max_length=255, null=True, verbose_name='Формат обучения'),
        ),
    ]