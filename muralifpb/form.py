# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth import authenticate

from muralifpb.models import User
from muralifpb.models import Login

class UserForm(forms.Form):
	firstName = forms.CharField(label='First name', max_length=50)
	lastName = forms.CharField(label='Last name', max_length=50)
	email = forms.EmailField(label='Email')

	def save(self, user=None):
		firstName = self.cleaned_data.get('firstName')
		lastName = self.cleaned_data.get('lastName')
		email = self.cleaned_data.get('email')

		if user:
			user.firstName = firstName
			user.lastName = lastName
			user.email = email
			user.save()
			return user

		user = User(firstName=firstName, lastName=lastName, email=email)
		user.save()
		return user

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

class LoginForm(forms.Form):
	login = forms.CharField(label='login', max_length=20)
	passwd = forms.CharField(label='passwd', max_length=40)

	def clean_login(self):
		login = self.cleaned_data.get('login')

		if Login.objects.filter(login=login):
			raise forms.ValidationError('Login existente')
		return 

class ClassName(object):
	pass