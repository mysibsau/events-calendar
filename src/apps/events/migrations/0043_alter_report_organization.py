# Generated by Django 3.2.7 on 2023-01-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_auto_20230130_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='organization',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ответственное подразделение'),
        ),
    ]
