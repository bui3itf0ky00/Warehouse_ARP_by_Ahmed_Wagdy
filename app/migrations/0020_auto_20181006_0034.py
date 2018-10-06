# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-05 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20181001_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RenameField(
            model_name='sellinvoice',
            old_name='product_description',
            new_name='invoice_description',
        ),
    ]