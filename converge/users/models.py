from django.db import models
from django.contrib.auth.models import User
import django.http.request

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #pics is the directory in the MEDIA directory to be saved
    image = models.ImageField(default='pics/default.png',upload_to='pics/') #needs pillow to be installed
    def __str__(self):
        return f'{self.user.username}\'s profile'
    def save(self):
        super().save()

class Project(models.Model):
      creator = models.CharField(max_length=100, default='testuser__')
      projectName = models.CharField(max_length=100)
      projectType = models.CharField(max_length=100)
      projectPicture = models.ImageField(default='pics/defaultProject.png',upload_to='pics/')
      def save(self):
          super().save()
