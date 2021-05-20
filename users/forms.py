from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# we use this form in user views
class UserRegister(UserCreationForm):
	email = forms.EmailField()

	""" nested name space for the configuration and keeps the configurations in one place. 
		within configurations, the model that is going to be affected is user model.
	"""
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	""" nested name space for the configuration and keeps the configurations in one place. 
		within configurations, the model that is going to be affected is user model.
	"""
	class Meta:
		model = User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']