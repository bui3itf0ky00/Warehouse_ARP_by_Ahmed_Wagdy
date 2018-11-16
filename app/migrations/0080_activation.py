# Generated by Django 2.1.2 on 2018-11-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial1', models.IntegerField()),
                ('serial2', models.IntegerField()),
                ('company', models.CharField(max_length=160)),
                ('last_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
