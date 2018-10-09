# Generated by Django 2.0.7 on 2018-08-18 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptodo', '0004_auto_20180813_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=(), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='created',
            field=models.DateTimeField(default='2018-08-18'),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='time_added',
            field=models.DateTimeField(default='2018-08-18'),
        ),
    ]