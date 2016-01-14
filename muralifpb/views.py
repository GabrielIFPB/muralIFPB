# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404


from muralifpb.models import User
from muralifpb.models import Login

from muralifpb.form import UserForm
from muralifpb.form import LoginForm

#def index(request):
#	return HttpResponse("Olá mundo!")
"""
def index(request):
	users = User.objects.all()

	if request.method == 'POST':
		firstName = request.POST.get('first_name')
		lastName = request.POST.get('last_name')
		email = request.POST.get('email')

		user = User(firstName=firstName, lastName=lastName, email=email)
		user.save()

		HttpResponseRedirect(reverse('index'))

	return render(request, 'index.html', {'users': users})
"""
def index(request):
	users = User.objects.all()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = UserForm()

	return render(request, 'index.html', 
		{
			'users': users,
			'form': form
		}
	)

def login(request):
	log = Login.objects.all()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			login = form.save()
			return HttpResponseRedirect(reverse('settings'))
	else:
		form = LoginForm()

	return render(request, 'login.html', {})

def settings(request):
	return render(request, 'settings.html', {})

def register(request):
	users = User.objects.all()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('register'))
	else:
		form = UserForm()

	return render(request, 'register.html', 
		{
			'users': users,
			'form': form
		}
	)

def search(request):
	users = User.objects.all()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('search'))
	else:
		form = UserForm()

	return render(request, 'search.html', 
		{
			'users': users,
			'form': form
		}
	)

def edit(request, id):
	user = get_object_or_404(User, id=id)
	initial = {
		'firstName': user.firstName,
		'lastName': user.lastName,
		'email': user.email
	}
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(user=user)
			return HttpResponseRedirect(reverse('settings'))
	else:
		form = UserForm(initial=initial)
	return render(request, 'edit.html', 
		{
			'user': user,
			'form': form
		}
	)