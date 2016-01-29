# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import authenticate

from muralifpb.models import User
from muralifpb.models import Login

##class UserForm(forms.Form):
##	firstName = forms.CharField(label='First name', max_length=50)
##	lastName = forms.CharField(label='Last name', max_length=50)
##	email = forms.EmailField(label='Email')
class UserForm(forms.ModelForm):
	matricula = forms.CharField(label='Matrícula')
	full_name = forms.CharField(label='Nome Completo')
	passwd = forms.CharField(label='Password', widget=forms.PasswordInput)
	email = forms.CharField(widget=forms.EmailInput)
	class Meta:
		model = User
		exclude = []
		#fields = [
		#			'matricula', 'full_name', 
		#			'email',     'login',   
		#			'passwd',
		#		]


	def save(self, user=None):
		matricula = self.cleaned_data.get('matricula')
		full_name = self.cleaned_data.get('full_name')
		email = self.cleaned_data.get('email')
		login = self.cleaned_data.get('login')
		passwd = self.cleaned_data.get('passwd')

		if user:
			user.matricula = matricula
			user.full_name = full_name
			user.email = email
			user.login = login
			user.passwd = passwd
			user.save()
			return user

		user = User(matricula=matricula, full_name=full_name, email=email,
					login=login, passwd=passwd
				)
		user.save()
		return user

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email):
			raise forms.ValidationError(_('Email já cadastrado!'))
		return email

	def clean_matricula(self):
		matricula = self.cleaned_data.get('matricula')

		if User.objects.filter(matricula=matricula):
			raise forms.ValidationError(_('matricula já cadastrado!'))
		return matricula

	def clean_login(self):
		login = self.cleaned_data.get('login')

		if User.objects.filter(login=login):
			raise forms.ValidationError(_('login já cadastrado!'))
		return login


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