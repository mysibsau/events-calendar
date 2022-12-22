# Generated by Django 3.2.7 on 2022-12-22 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_auto_20221221_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_fact', models.DateField(verbose_name='Дата начала Факт')),
                ('stop_date_fact', models.DateField(verbose_name='Дата конца Факт')),
                ('place_fact', models.CharField(max_length=512)),
                ('coverage_participants_fact', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Охват участников (факт)')),
                ('links', models.TextField(blank=True, verbose_name='Ссылки на материалы в интернете о мероприятии (факт)')),
                ('organizators', models.ManyToManyField(blank=True, null=True, to='events.Organiztor')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='events.report'),
        ),
    ]