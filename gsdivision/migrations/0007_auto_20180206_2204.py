# Generated by Django 2.0.1 on 2018-02-06 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsdivision', '0006_auto_20180206_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 22, 4, 0, 609465), verbose_name='සේවය අවසන් කල දිනය '),
        ),
    ]
