# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-14 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20181014_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='da2en',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='daily',
            name='maden',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='daily',
            name='total_da2en',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='daily',
            name='total_maden',
            field=models.IntegerField(default=0),
        ),
    ]
