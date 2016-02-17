# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	facebook = models.URLField()
	birth = models.DateField()

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField(max_length=250)
	category = models.ManyToManyField(Category)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=100)
	comment = models.TextField(max_length=250)
	post = models.OneToOneField(Post)

	def __unicode__(self):
		return self.author

class UserStudent(models.Model):

	user = models.OneToOneField(
		User,
		verbose_name=u'Usuário',
		related_name=u'Usuarios',
		unique=True
	)

	matricula = models.CharField(
		max_length=10,
		unique=True
	)

	email = models.EmailField(
		max_length=200,
		unique=True
	)
	
	def __unicode__(self):
		return  self.matricula