# Generated by Django 2.1.7 on 2019-04-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userDescription',
            field=models.CharField(default='tell us about yourself', max_length=1000, verbose_name='User description'),
        ),
        migrations.AddField(
            model_name='profile',
            name='userInterests',
            field=models.CharField(default='tell us about yourself', max_length=250, verbose_name='User interests'),
        ),
    ]