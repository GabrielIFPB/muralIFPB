# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

from muralifpb.models import UserStudent
from muralifpb.form import user_inline

from muralifpb.models import News
from muralifpb.models import Category
from muralifpb.form import CategoryForm
from muralifpb.models import Post
from muralifpb.form import PostForm
from muralifpb.models import NewsPortals
from muralifpb.form import NewsPortalsForm

def index(request):
	#posts = Post.published_objects.all()
	#posts = Post.objects.filter(published=True)
	#news = News.objects.filter(published=True)

	return render(request, 'index.html', 
		{
			#'news' : news,
			#'posts' : posts,
		}
	)

def register(request):
	users = UserStudent.objects.all()

	if request.method == 'POST':
		user_form = user_inline(request.POST)
		user_django = UserCreationForm(request.POST)
		if form.is_valid():
			user = user_form.save()
			django = user_django.save()
			return HttpResponseRedirect(reverse('register'))
	else:
		user_form = user_inline()
		user_django = UserCreationForm()

	return render(request, 'register.html', 
		{
			'users': UserCreationForm,
			'form': user_inline,
		}
	)

def add_category(request):
	categories = Category.objects.all()

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save()
			return HttpResponseRedirect(reverse('add_category'))
	else:
		form = CategoryForm()

	return render(request, 'add_category.html', 
		{
			'categories': categories,
			'form': form,
		}
	)

def edit_category(request, id):
	category = get_object_or_404(Category, id=id)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			category = form.save()
			return HttpResponseRedirect(reverse('add_category'))
	else:
		form = CategoryForm(instance=category)

	return render(request, 'add_category.html', 
		{
			'category': category,
			'form': form,
		}
	)

@login_required
def delete_category(request, id):
	category = get_object_or_404(Category, id=id)
	category.delete()
	return HttpResponseRedirect(reverse('add_category'))

def add_post(request):
	posts = Post.objects.all()

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(reverse('add_post'))
	else:
		form = PostForm()

	return render(request, 'add_post.html',
		{
			'posts': posts,
			'form': form,
		}
	)

def edit_post(request, id):
	post = get_object_or_404(Post, id=id)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(reverse('add_post'))
	else:
		form = PostForm(instance=post)

	return render(request, 'add_post.html',
		{
			'post': post,
			'form': form,
		}
	)

@login_required
def delete_post(request, id):
	post = get_object_or_404(Post, id=id)
	post.delete()
	return HttpResponseRedirect(reverse('add_post'))

def add_portal(request):
	portals = NewsPortals.objects.all()

	if request.method == 'POST':
		form = NewsPortalsForm(request.POST)
		if form.is_valid():
			portal = form.save()
			return HttpResponseRedirect(reverse('add_portal'))
	else:
		form = NewsPortalsForm()

	return render(request, 'add_portal.html',
		{
			'portals': portals,
			'form': form,
		}
	)

def edit_portal(request, id):
	portal = get_object_or_404(NewsPortals, id=id)

	if request.method == 'POST':
		form = NewsPortalsForm(request.POST, instance=portal)
		if form.is_valid():
			portal = form.save()
			return HttpResponseRedirect(reverse('edit_portal'))
	else:
		form = NewsPortalsForm(instance=portal)

	return render(request, 'edit_portal.html',
		{
			'portal': portal,
			'form': form,
		}
	)

@login_required
def delete_portal(request, id):
	portal = get_object_or_404(NewsPortals, id=id)
	portal.delete()
	return HttpResponseRedirect(reverse('add_portal'))

@login_required
def exit(request):
	logout(request)