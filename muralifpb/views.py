# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate

from muralifpb.models import UserMy
from muralifpb.form import UserStudentForm
from muralifpb.form import UserForm

from muralifpb.models import News
from muralifpb.models import Category
from muralifpb.form import CategoryForm
from muralifpb.models import Post
from muralifpb.form import PostForm
from muralifpb.models import NewsPortals
from muralifpb.form import NewsPortalsForm

def index(request):
	print(request)
	return render(request, 'index.html', {})

@login_required
def account(request):
	context = {
			'posts' : Post.unpublished_objects.filter(author_id=request.user.id),
			'unposts': Post.published_objects.filter(author_id=request.user.id),
		}
	return render(request, 'account.html', context)

@login_required
def register(request):
	context = {}
	if request.method == 'POST' and request.user.is_staff:
		form = UserStudentForm(request.POST)
		if form.is_valid():
			user = form.save()
			context['success'] = True
	else:
		form = UserStudentForm()
	context['form'] = form
	return render(request, 'register.html', context)

@login_required
def edit_password(request):
	context = {}
	if request.method == 'POST' and request.user.is_authenticated():
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)
	context['form'] = form
	return render(request, 'edit_password.html', context)

@login_required
def edit_user(request):
	user = get_object_or_404(UserMy, pk=request.user.id)
	context = {}
	if request.method == 'POST' and request.user.is_authenticated():
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			user = form.save()
			context['success'] = True
	else:
		form = UserForm(instance=user)
	context['form'] = form
	return render(request, 'edit_user.html', context)

@login_required
def search(request):
	users = UserMy.objects.all()

	return render(request, 'search.html',
		{
			'users' : users,
		}
	)	

@login_required
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

@login_required
def edit_category(request, id=None):
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

@login_required
def add_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author_id = request.user.id
			post.save()
			return HttpResponseRedirect(reverse('add_post'))
	else:
		form = PostForm()

	return render(request, 'add_post.html',
		{
			'form': form,
		}
	)

@login_required
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
	if request.user.is_authenticated() and request.user.id == post.author_id:
		post.delete()
	return HttpResponseRedirect(reverse('account'))

@login_required
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

@login_required
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