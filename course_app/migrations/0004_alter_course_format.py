# Generated by Django 4.1.3 on 2022-11-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_alter_course_certificate_alter_course_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='format',
            field=models.CharField(choices=[(1, 'оффлайн'), (2, 'онлайн')], default=1, max_length=255, null=True, verbose_name='Формат обучения'),
        ),
    ]
