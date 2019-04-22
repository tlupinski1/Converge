# Generated by Django 2.1.7 on 2019-04-22 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('members_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PollAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('answerOne', models.IntegerField(default=0)),
                ('answerTwo', models.IntegerField(default=0)),
                ('answerThree', models.IntegerField(default=0)),
                ('answerFour', models.IntegerField(default=0)),
                ('answerFive', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('polls_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Enter a Title for your Poll', max_length=120)),
                ('questionOne', models.CharField(default='Enter a Question', max_length=120)),
                ('questionTwo', models.CharField(default='Enter a Question', max_length=120)),
                ('questionThree', models.CharField(default='Enter a Question', max_length=120)),
                ('questionFour', models.CharField(default='Enter a Question', max_length=120)),
                ('questionFive', models.CharField(default='Enter a Question', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='pics/default.png', upload_to='pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.CharField(max_length=100)),
                ('projectName', models.CharField(max_length=100)),
                ('projectType', models.CharField(max_length=100)),
                ('projectDescription', models.CharField(max_length=500)),
                ('textArea', models.TextField(default='add info / planning here', max_length=10000)),
                ('projectPicture', models.ImageField(default='pics/defaultProject.png', upload_to='pics/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='polls',
            name='creator',
            field=models.ForeignKey(default='Not Logged IN', on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='pollanswers',
            name='polls_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Polls'),
        ),
        migrations.AddField(
            model_name='pollanswers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='members',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='members',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Project'),
        ),
        migrations.AddField(
            model_name='links',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Project'),
        ),
        migrations.AddField(
            model_name='files',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Project'),
        ),
    ]
