# Generated by Django 3.2.7 on 2023-01-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_alter_organiztor_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='count_index',
        ),
        migrations.RemoveField(
            model_name='event',
            name='is_transferred',
        ),
        migrations.AddField(
            model_name='event',
            name='original_author',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Изначальный автор'),
        ),
        migrations.AddField(
            model_name='report',
            name='count_index',
            field=models.TextField(default='', verbose_name='Колличественный показатель'),
        ),
    ]
