from django.db import models

from users.models import Profile

# Create your models here.
class Polls(models.Model):
    polls_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    questions = models.CharField(max_length=120)
    
