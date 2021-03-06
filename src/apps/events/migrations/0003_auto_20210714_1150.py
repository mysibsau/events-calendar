# Generated by Django 3.2.5 on 2021-07-14 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20210714_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='verified',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_verifications', to=settings.AUTH_USER_MODEL, verbose_name='Кто верифицировал'),
        ),
        migrations.AlterField(
            model_name='event',
            name='verified_date',
            field=models.DateField(blank=True, verbose_name='Дата верификации'),
        ),
    ]
