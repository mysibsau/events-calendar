# Generated by Django 3.2.7 on 2023-01-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_alter_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
    ]
