# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-01 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20180930_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.CharField(max_length=260)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Supplier')),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='product',
        ),
        migrations.DeleteModel(
            name='InvoiceType',
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='item_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]