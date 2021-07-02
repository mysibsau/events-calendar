# Generated by Django 3.2.5 on 2021-07-02 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_request_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='participant',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='participant',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания'),
        ),
    ]