# post_save is the signal which gets triggered once an object is saved
from django.db.models.signals import post_save

# user model is called sender because it is the one which sends the signal
from django.contrib.auth.models import User

# receiver is the one which does the task
from django.dispatch import receiver

from .models import Profile

#to be run whenever a new user is created
# whenever a user object is saved, sender sends the signal and receiver receiives the signal and initiates the process
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()
