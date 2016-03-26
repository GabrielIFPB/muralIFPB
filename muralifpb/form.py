# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

from django.utils.translation import ugettext_lazy as _

from muralifpb.models import UserStudent
from muralifpb.models import Category
from muralifpb.models import Post
from muralifpb.models import NewsPortals


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		exclude = [u'last_login', u'date_joined', u'password', ]
		#fields = [u'username', u'first_name', u'last_name', u'is_staff']

class UserStudentForm(forms.ModelForm):

	class Meta:
		model = UserStudent
		exclude = [u'user', ]
	"""
	def clean_matricula(self):
		matricula = self.cleaned_data.get(u'matricula')

		if UserStudent.objects.filter(matricula=matricula):
			raise forms.ValidationError(u'matricula existente!')
		return matricula
	
	def clean_email(self):
		email = self.cleaned_data.get(u'email')

		if UserStudent.objects.filter(email=email):
			raise forms.ValidationError(u'Email existente!')
		return email
	"""

user_inline = inlineformset_factory(User, UserStudent, UserStudentForm, exclude=[], can_delete=False, )

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		exclude = []
		label = {
			'name': _('Writer'),
		}
		help_texts = {
			'name': _('Some useful help text.'),
		}
		error_messages = {
			'name': {
				'max_length': _("This writer's name is too long."),
			},
		}
	
	def clean_name(self):
		name = self.cleaned_data.get(u'name')

		if Category.objects.filter(name=name):
			raise forms.ValidationError(u'Categoria existente!')
		return name
	
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		exclude = [u'author']

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