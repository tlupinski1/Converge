from django.db.models.signals import post_save
#post_save - signal after object gets Created
from django.contrib.auth.models import User

from django.dispatch import receiver
#receiver is like the event listener for the signal.
from .models import Profile

#create new profile for each user
@receiver(post_save, sender=User) #sender is the User.  so if the user gets post_saved then send signal.  which will run create_profile function
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) #create profile object from the user.

@receiver(post_save, sender=User) #sender is the User.  so if the user gets post_saved then send signal.  which will run create_profile function
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
