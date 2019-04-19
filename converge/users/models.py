from django.db import models
from django.contrib.auth.models import User
import django.http.request


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #pics is the directory in the MEDIA directory to be saved
    image = models.ImageField(default='pics/default.png',upload_to='pics/') #needs pillow to be installed
    def __str__(self):
        return f'{self.user.username}\'s profile'
    def save(self,**kwargs):
        super().save()

class Project(models.Model):
      dateTime = models.CharField(max_length=100)
      creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
      projectName = models.CharField(max_length=100)
      projectType = models.CharField(max_length=100)
      textArea = models.TextField(max_length=10000,default="add info / planning here")
      projectPicture = models.ImageField(default='pics/defaultProject.png',upload_to='pics/')
      def save(self, **kwargs):
          super().save()

class Files(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    file = models.CharField(max_length=100)
    def save(self, **kwargs):
        super().save()

class Links(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    def save(self, **kwargs):
        super().save()

class Polls(models.Model):
    polls_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, default='Enter a Title for your Poll')
    questionOne = models.CharField(max_length=120, default='Enter a Question')
    questionTwo = models.CharField(max_length=120, default='Enter a Question')
    questionThree = models.CharField(max_length=120, default='Enter a Question')
    questionFour = models.CharField(max_length=120, default='Enter a Question')
    questionFive = models.CharField(max_length=120, default='Enter a Question')
