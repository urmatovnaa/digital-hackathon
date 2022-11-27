# Generated by Django 4.1.3 on 2022-11-27 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='course_photo', verbose_name='Фото')),
                ('time_study', models.CharField(choices=[('оффлайн', 'оффлайн'), ('онлайн', 'онлайн')], default=1, max_length=255, verbose_name='Формат обучения')),
                ('duration', models.CharField(max_length=255, verbose_name='Продолжительность курса')),
                ('certificate', models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], default=1, max_length=255, verbose_name='Сертификат по окончании')),
                ('overview', models.TextField(verbose_name='Описание курса')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.category', verbose_name='Категория')),
                ('contributors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event_app.speaker', verbose_name='Преподаватели')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
