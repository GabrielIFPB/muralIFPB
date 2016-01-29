# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import authenticate

from muralifpb.models import UserProfile
#from muralifpb.models import Login

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = UserProfile
		#exclude = []
		fields = ['first_name', 'last_name', 'email', 'username', 'password']

	def save(self, user=None):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if user:
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.set_password
			user.save()
			return user

		user = UserAdmin(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		return user

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if UserProfile.objects.filter(email=email):
			raise forms.ValidationError('Email já cadastrado!')
		return email

	def clean_firstName(self):
		firstName = self.cleaned_data.get('firstName')

		if UserProfile.objects.filter(firstName=firstName):
			raise forms.ValidationError('log já cadastrado!')
		return firstName

'''
class LoginForm(forms.Form):
	login = forms.CharField(label='login', max_length=20)
	passwd = forms.CharField(label='passwd', max_length=40)

	def clean_login(self):
		login = self.cleaned_data.get('login')

		if not User.objects.filter(username=login):
			raise forms.ValidationError('Login inexistente')
		return login

	def clean_passwd(self):
		login = self.cleaned_data.get('login')
		passwd = self.cleaned_data.get('password')

		if not authenticate(username=login, password=passwd):
			raise forms.ValidationError('password error')
		return passwd

	def save(self):
		login = self.cleaned_data.get('login')
		passwd = self.cleaned_data.get('password')
		return authenticate(username=login, password=passwd)
'''