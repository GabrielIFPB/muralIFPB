# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import authenticate

#from muralifpb.models import User
from muralifpb.models import Login

##class UserForm(forms.Form):
##	firstName = forms.CharField(label='First name', max_length=50)
##	lastName = forms.CharField(label='Last name', max_length=50)
##	email = forms.EmailField(label='Email')
class UserForm(forms.ModelForm):
	class Meta:
		model = UserAdmin
		#exclude = []
		fields = ['first_name', 'last_name', 'email', 'username', 'password']

'''
	def save(self, user=None):
		firstName = self.cleaned_data.get('firstName')
		lastName = self.cleaned_data.get('lastName')
		email = self.cleaned_data.get('email')
		login = self.cleaned_data.get('login')
		passwd = self.cleaned_data.get('passwd')

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

		if UserAdmin.objects.filter(email=email):
			raise forms.ValidationError('Email já cadastrado!')
		return email

	def clean_firstName(self):
		firstName = self.cleaned_data.get('firstName')

		if UserAdmin.objects.filter(firstName=firstName):
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