# Generated by Django 3.2.7 on 2023-01-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_auto_20230130_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organiztor',
            name='position',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
