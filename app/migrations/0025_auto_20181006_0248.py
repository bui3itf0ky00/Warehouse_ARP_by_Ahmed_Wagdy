# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-06 00:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0024_auto_20181006_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellinvoice',
            name='source',
            field=models.CharField(default='الرئيسية', max_length=180),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]