# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from muralifpb.models import UserStudent
from muralifpb.form import user_inline

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
	return render(request, 'index.html', { })

@login_required
def account(request):
	posts = Post.published_objects.filter(author_id=request.user.id)
	unposts = Post.unpublished_objects.filter(author_id=request.user.id)
	#print request.COOKIES
	return render(request, 'account.html', 
		{
			'posts' : posts,
			'unposts': unposts,
		}
	)

@login_required
def register(request):
	if request.method == 'POST' and request.user.is_staff:
		user_django = UserCreationForm(request.POST)
		if user_django.is_valid():
			django = user_django.save()
			user_form = user_inline(request.POST, instance=django)
			if user_form.is_valid():
				user = user_form.save()
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

@login_required
def edit_user(request):
	user = get_object_or_404(User, id=request.user.id)
	userStudent = UserStudent.objects.get(user_id=request.user.id)

	if request.method == 'POST' and request.user.is_authenticated():
		form = UserStudentForm(request.POST, instance=userStudent)
		user_form = UserForm(request.POST, instance=user)
		if form.is_valid() and user_form.is_valid():
			user_form.save()
			userStudent = form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = UserStudentForm(instance=userStudent)
		user_form = UserForm(instance=user)

	return render(request, 'edit_user.html',
		{
			'user_form' : user_form,
			'form': form,
		}
	)

@login_required
def search(request):
	users = UserStudent.objects.all()

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
		form = PostForm(request.POST)
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