# Generated by Django 2.1.7 on 2019-04-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190423_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userInterests',
            field=models.CharField(default='list your interests', max_length=250, verbose_name='User interests'),
        ),
    ]