# Generated by Django 2.0.7 on 2018-09-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0006_auto_20180820_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoapp',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='todoapp',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='todoapp',
            name='time_added',
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='created',
            field=models.DateTimeField(default='2018-09-06'),
        ),
    ]
