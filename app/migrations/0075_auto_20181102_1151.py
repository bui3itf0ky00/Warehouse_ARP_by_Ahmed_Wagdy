# Generated by Django 2.1.2 on 2018-11-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0074_talabat_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talabat',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
