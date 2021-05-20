from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegister,UserUpdateForm,ProfileUpdateForm


def register(request):
	if request.method == "POST":
		form = UserRegister(request.POST)
		if form.is_valid():
			form.save() #saving the user if the entered data is valid
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to log in ')
			return redirect('login')
	else:
		form = UserRegister()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		
		if u_form.is_valid() and u_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile') # this will actually send a get request without actually reloading it

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}
	return render(request,'users/profile.html',context)
