# Generated by Django 2.1.7 on 2019-04-20 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190420_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userDescription',
        ),
    ]