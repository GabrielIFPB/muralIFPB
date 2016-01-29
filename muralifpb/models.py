# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User as UserAdmin

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

class User(models.Model):
	matricula = models.CharField(max_length=50)
	full_name = models.CharField(max_length=200)
	email = models.EmailField()
	login = models.CharField(max_length=30)
	passwd = models.CharField(max_length=30)

	def __unicode__(self):
		return '%s %s'(self.matricula, self.full_name)

class Login(models.Model):
	userAdmin = models.OneToOneField(UserAdmin, related_name='user_profile')

	def __unicode__(self):
		return self.userAdmin.username