# Generated by Django 3.2.7 on 2022-08-18 05:04

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Автор'), (1, 'Модератор'), (2, 'Администратор')], default=0, verbose_name='Роль'),
        ),
    ]
