# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

from muralifpb.models import UserStudent
<<<<<<< HEAD
from muralifpb.models import Category
from muralifpb.models import Post
from muralifpb.models import NewsPortals

user_inline = inlineformset_factory(User, UserStudent,  exclude=[])

=======

user_inline = inlineformset_factory(User, UserStudent,  exclude=[])

class UserForm(forms.Form):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = UserStudent
		#exclude = []
		#fields = [u'first_name', u'last_name', u'email', u'username', u'password']

	def clean_username(self):
		username = self.cleaned_data.get(u'username')

		if User.objects.filter(username=username):
			raise forms.ValidationError(u'existente')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email):
			raise forms.ValidationError('Email já cadastrado!')
		return email

	def clean_firstName(self):
		firstName = self.cleaned_data.get('firstName')

		if User.objects.filter(firstName=firstName):
			raise forms.ValidationError('log já cadastrado!')
		return firstName


>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
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
<<<<<<< HEAD

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		exclude = []
		#fields = []

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		exclude = []

class NewsPortalsForm(forms.ModelForm):

	class Meta:
		model = NewsPortals
		exclude = []			
=======
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
