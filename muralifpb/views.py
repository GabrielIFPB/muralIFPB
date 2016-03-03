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

def register(request):
	users = UserStudent.objects.all()

	if request.method == 'POST':
		form = user_inline(request.POST)
		user_form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('register'))
	else:
		form = user_inline()
		user_form = UserCreationForm()

	return render(request, 'register.html', 
		{
			'users': UserCreationForm,
			'form': user_inline,
		}
	)

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