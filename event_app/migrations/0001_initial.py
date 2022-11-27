# Generated by Django 4.1.3 on 2022-11-27 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('photo', models.ImageField(upload_to='event_photo', verbose_name='Фото')),
                ('time', models.CharField(max_length=255, verbose_name='Время')),
                ('description', models.TextField(verbose_name='Чему вы научитесь?')),
                ('about', models.TextField(verbose_name='О программе')),
                ('number_for_seats', models.IntegerField(verbose_name='Количество мест')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='ФИО')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Спикер',
                'verbose_name_plural': 'Спикеры',
            },
        ),
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people_count', to='event_app.event', verbose_name='Мероприятие')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='speakers_detail',
            field=models.ManyToManyField(blank=True, related_name='speakers_detail', to='event_app.speaker', verbose_name='Спикеры'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
