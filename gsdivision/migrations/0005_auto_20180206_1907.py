# Generated by Django 2.0.1 on 2018-02-06 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsdivision', '0004_auto_20180206_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 19, 7, 58, 993953), verbose_name='සේවය අවසන් කල දිනය '),
        ),
    ]
