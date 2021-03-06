# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-06 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181006_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description10',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description2',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description3',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description4',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description5',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description6',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description7',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description8',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='invoice_description9',
            field=models.CharField(blank=True, default='البيان', max_length=260),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price10',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price2',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price3',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price4',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price5',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price6',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price7',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price8',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='price9',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product10',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product10', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product2', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product3',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product3', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product4',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product4', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product5',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product5', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product6',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product6', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product7',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product7', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product8',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product8', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='product9',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product9', to='app.Product'),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity10',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity2',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity3',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity4',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity5',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity6',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity7',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity8',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='quantity9',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sellinvoice',
            name='invoice_description',
            field=models.CharField(default='البيان', max_length=260),
        ),
        migrations.AlterField(
            model_name='sellinvoice',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sellinvoice',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
