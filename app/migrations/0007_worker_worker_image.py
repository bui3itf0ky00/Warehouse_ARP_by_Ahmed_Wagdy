# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-27 11:47
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180927_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='worker_image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='media'),
        ),
    ]
