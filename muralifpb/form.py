# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.utils.translation import ugettext_lazy as _

from muralifpb.models import UserMy
from muralifpb.models import Category
from muralifpb.models import Post
from muralifpb.models import NewsPortals

User = get_user_model()

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [u'username', u'name', u'email', u'image']

		def clean_email(self):
			email = self.cleaned_data.get(u'email')
			queryset =  User.objects.filter(email=email).exlude(pk=self.instance.pk)
			
			if queryset.exists():
				raise forms.ValidationError(u'Já existe um aluno com essa matricula.')
			return email

class UserStudentForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [u'matricula', u'username', u'email', u'is_staff', u'is_reitoria']
	
	password1 = forms.CharField(
			label='Senha',
			widget=forms.PasswordInput,
		)
	password2 = forms.CharField(
			label='Confirmação de Senha',
			widget=forms.PasswordInput,
		)
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password2 and password1 and password2 != password1:
			raise forms.ValidationError(
					self.error_messages['password_mismatch'],
					code='password_mismatch',
				)
		return password2

	def save(self, commit=True):
		user = super(UserStudentForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

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