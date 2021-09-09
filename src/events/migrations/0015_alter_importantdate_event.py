# Generated by Django 3.2.7 on 2021-09-09 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_rename_importantdates_importantdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importantdate',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='important_dates', to='events.event', verbose_name='Мероприятие'),
        ),
    ]
