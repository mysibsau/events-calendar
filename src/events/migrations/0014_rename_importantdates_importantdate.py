# Generated by Django 3.2.7 on 2021-09-09 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_importantdates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImportantDates',
            new_name='ImportantDate',
        ),
    ]
