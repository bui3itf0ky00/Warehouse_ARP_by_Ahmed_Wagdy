# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-05 22:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_auto_20181006_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainFinanceMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('withdrawal', 'سحب'), ('deposite', 'إيداع')], default='1', max_length=9)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=800)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
