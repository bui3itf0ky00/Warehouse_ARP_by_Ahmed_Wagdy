# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-14 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20181015_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='total_da2en',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='total_maden',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
