# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.forms.models import inlineformset_factory

from muralifpb.form import UserForm

def index(request):
	return render(request, 'index.html', { })

def settings(request):
	return render(request, 'settings.html', { })

def register(request):

	user_inline = inlineformset_factory(UserStudent, UserAdmin, UserForm)
	users = UserStudent.objects.all()

	if request.method == 'POST':
		form = UserStudent(request.POST)
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
"""
def search(request):
	users = UserAdmin.objects.all()
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
	user = get_object_or_404(UserAdmin, id=id)
	initial = {
		'first_name' : user.first_name,
		'last_name'  : user.last_name,
		'email'      : user.email,
		'username'   : user.username,
		'password'   : user.password
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
"""
def exit(request):
	logout(request)
