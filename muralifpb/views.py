# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

<<<<<<< HEAD
from muralifpb.models import UserStudent
from muralifpb.form import user_inline

from muralifpb.models import Category
from muralifpb.form import CategoryForm
from muralifpb.models import Post
from muralifpb.form import PostForm
from muralifpb.models import NewsPortals
from muralifpb.form import NewsPortalsForm

def index(request):
	return render(request, 'index.html', { })

=======
from muralifpb.form import UserForm
from muralifpb.models import UserStudent
from muralifpb.form import user_inline

def index(request):
	return render(request, 'index.html', { })

def settings(request):
	return render(request, 'settings.html', { })

>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
def register(request):
	users = UserStudent.objects.all()

	if request.method == 'POST':
<<<<<<< HEAD
		form = user_inline(request.POST)
		user_form = UserCreationForm(request.POST)
=======
		form = UserForm(request.POST)
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('register'))
	else:
<<<<<<< HEAD
		form = user_inline()
		user_form = UserCreationForm()
=======
		form = UserForm()
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0

	return render(request, 'register.html', 
		{
			'users': UserCreationForm,
			'form': user_inline,
		}
	)
<<<<<<< HEAD

def add_category(request):
	category = Category.objects.all()

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save()
			return HttpResponseRedirect(reverse('addcategory'))
	else:
		form = CategoryForm()

	return render(request, 'add_category.html', 
		{
			'form': form,
		}
	)

def add_post(request):
	posts = Post.objects.all()

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(reverse('addpost'))
	else:
		form = PostForm()

	return render(request, 'add_post.html',
		{
			'form': form,
		}
	)

def add_portal(request):
	portals = NewsPortals.objects.all()

	if request.method == 'POST':
		form = NewsPortalsForm(request.POST)
		if form.is_valid():
			portal = form.save()
			return HttpResponseRedirect(reverse('addportal'))
	else:
		form = NewsPortalsForm()

	return render(request, 'add_portal.html',
		{
			'form': form,
		}
	)

def exit(request):
	logout(request)
=======
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
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
