# Generated by Django 3.2.7 on 2023-01-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_event_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_transferred',
            field=models.BooleanField(default=False, verbose_name='Переданно ли мероприятие'),
        ),
    ]
