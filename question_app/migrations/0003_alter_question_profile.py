# Generated by Django 4.1.3 on 2022-11-26 21:19

import account_app.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_app', '0002_answer_question_delete_guide_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='profile',
            field=models.ImageField(default=account_app.managers.get_default_profile_image, upload_to='avatar', verbose_name='Aватар'),
        ),
    ]
