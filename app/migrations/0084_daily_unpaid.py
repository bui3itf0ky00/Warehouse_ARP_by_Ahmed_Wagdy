# Generated by Django 2.2 on 2019-04-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0083_auto_20190430_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='unpaid',
            field=models.IntegerField(default=0),
        ),
    ]
