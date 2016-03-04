# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

from muralifpb.models import UserStudent
from muralifpb.models import Category
from muralifpb.models import Post
from muralifpb.models import NewsPortals

user_inline = inlineformset_factory(User, UserStudent,  exclude=[])

class LoginForm(forms.Form):
	username = forms.CharField(label=u'login', max_length=20)
	password = forms.CharField(label=u'password', max_length=40)

	def clean_username(self):
		username = self.cleaned_data.get(u'username')

		if not User.objects.filter(username=username):
			raise forms.ValidationError(u'Login inexistente')
		return username

	def clean_password(self):
		username = self.cleaned_data.get(u'username')
		password = self.cleaned_data.get(u'password')

		if not authenticate(username=username, password=password):
			raise forms.ValidationError(u'password error')
		return password

	def save(self):
		username = self.cleaned_data.get(u'username')
		password = self.cleaned_data.get(u'password')
		return authenticate(username=username, password=password)

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		exclude = []
	
	def clean_name(self):
		name = self.cleaned_data.get(u'name')

		if Category.objects.filter(name=name):
			raise forms.ValidationError(u'Categoria existente!')
		return name
	

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		exclude = []

class NewsPortalsForm(forms.ModelForm):

	class Meta:
		model = NewsPortals
		exclude = []

	def clean_name(self):
		name = self.cleaned_data.get(u'name')

		if NewsPortals.objects.filter(name=name):
			raise forms.ValidationError(u'Já existe um portal com esse nome!')
		return name

	def clean_link(self):
		link = self.cleaned_data.get(u'link')

		if NewsPortals.objects.filter(link=link):
			raise forms.ValidationError(u'Esse link já existe!')
		return link