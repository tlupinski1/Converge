from django.db import models

class User(models.Model): #one table
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  def __str__(self):
    return self.username;

# Create your models here.
