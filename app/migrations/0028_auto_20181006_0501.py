# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-06 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_sellinvoice_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellinvoice',
            name='notes',
            field=models.TextField(blank=True, default='ملاحظات', max_length=1200),
        ),
    ]
