from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):

	if request.method == 'post':
		request.post.get('name')
		request.post.get('password')

		user = authenticate(request, username=name, password=password)

		if user is not None:
			Login(request, user)
			return redirect('flux')	

	return render(request, 'home/home.html')


def registration(request):
	form = UserCreationForm()

	if request.method == 'post':
		form = UserCreationForm(request.post)
		if form.is_valid():
			form.save()
			user_name = form.cleaned_data.get('username')
			messages.success(request, 'Votre compte "' + user_name 
				+ '" est bien enregistré')

			return redirect('home')

	context = {'form': form}

	return render(request, 'registration/inscription.html', context)