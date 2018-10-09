# Generated by Django 2.0.7 on 2018-10-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('comment', models.CharField(max_length=30)),
                ('time_added', models.DateTimeField(default='2018-10-05')),
            ],
            options={
                'ordering': ['-time_added'],
            },
        ),
    ]