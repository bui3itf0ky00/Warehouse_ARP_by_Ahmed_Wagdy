# Generated by Django 2.1.2 on 2018-11-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_warehouse_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farm'),
        ),
    ]
