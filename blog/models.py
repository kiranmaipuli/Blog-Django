from django.db import models
from django.utils import timezone
from django.urls import reverse

# Django by default has user model. so, we are directly importing the user model here
from django.contrib.auth.models import User

# User model and Post model are related to each other. Each and every post belongs to one user. so user and post have one to many relationship

# tables are treated as classes in Django. we follow object oriented structure for accessing and storing data

# we are creating a model called Post and inherit from models
class Post(models.Model):
	#adding fields to this model

	# title is a field of Post. It is a character field with maximum length as 100
	title = models.CharField(max_length=100)
	# TextField - unrestricted text
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# if a User is deleted, then posts related to that author is also deleted. That is the deletion is propogated to the posts 
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})