from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #delete user delete images.  also each user gets one profile
    image = models.ImageField(default='/pics/default.png',upload_to='pics') #needs pillow to be installed
    def __str__(self):
        return f'{self.user.username}\'s profile'
