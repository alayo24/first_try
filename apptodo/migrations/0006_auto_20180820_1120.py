# Generated by Django 2.0.7 on 2018-08-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0005_auto_20180818_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='created',
            field=models.DateTimeField(default='2018-08-20'),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='time_added',
            field=models.DateTimeField(default='2018-08-20'),
        ),
    ]