# -*- coding: UTF-8 -*-
from django.db import models

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
	firstName = models.CharField('First name', max_length=50, blank=False)
	lastName = models.CharField(max_length=50)
	email = models.EmailField()
	#facebook = models.URLField()

	def __unicode__(self):
		return '%s %s'(self.firstName, self.lastName)

class Login(models.Model):
	login = models.CharField(max_length=20)
	passwd = models.CharField(max_length=40)

	def __unicode__(self):
		return self.login