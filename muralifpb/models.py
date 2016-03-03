# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserStudent(models.Model):

	matricula = models.CharField(
			verbose_name='Matricula',
			max_length=30,
			unique=True,
		)
	email = models.EmailField(
			verbose_name='Email',
			max_length=200,
			unique=True,
		)
	user = models.OneToOneField(
			User,
			verbose_name=u'Usuário',
			related_name=u'Usuarios',
			unique=True,
		)

	def __unicode__(self):
		return  self.matricula

class Category(models.Model):

	class Meta:
		verbose_name = u'Categoria'
		verbose_name_plural = u'Categorias'
		ordering = [u'name']

	name = models.CharField(
			u'Nome',
			max_length=100,
		)
	published = models.BooleanField(
			u'Publicado',
			default=True,
		)
	# Audit fields
	created_on = models.DateTimeField(
			u'Criado em',
			auto_now_add=True,
		)
	updated_on = models.DateTimeField(
			u'Atualizado em',
			auto_now=True,
		)
=======

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	facebook = models.URLField()
	birth = models.DateField()

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0

	def __unicode__(self):
		return self.name

class Post(models.Model):
<<<<<<< HEAD

	class Meta:
		verbose_name = u'Post'
		verbose_name_plural = u'Posts'
		#ordena do mais novo para o mais antigo
		ordering = [u'created_on']
		#ordena do mais antigo para o mais novo
		#ordering = [u'-created_on']

	user = models.ForeignKey(
			UserStudent,
			verbose_name=u'Postado por',
		)
	title = models.CharField(
			u'Título',
			max_length=100,
		)
	text = models.TextField(
			u'Texto',
		)
	category = models.ForeignKey(
			Category,
			verbose_name=u'categoria',
			related_name=u'posts'
		)
	published = models.BooleanField(
			u'Publicado',
			default=True,
		)
	# Audit fields
	created_on = models.DateTimeField(
			u'Criado em',
			auto_now_add=True,
		)
	updated_on = models.DateTimeField(
			u'Atualizado em',
			auto_now=True,
		)
=======
	title = models.CharField(max_length=100)
	text = models.TextField(max_length=250)
	category = models.ManyToManyField(Category)
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0

	def __unicode__(self):
		return self.title

<<<<<<< HEAD
class NewsPortals(models.Model):

	name = models.CharField(
			u'Nome do protal de notícia',
			max_length=100,
		)
	link = models.URLField(
			u'Fonte da notícia',
			max_length=200,
		)

	def __unicode__(self):
		return self.name

class News(models.Model):

	class Meta:
		verbose_name = u'Notícia'
		verbose_name_plural = u'Notícias'

	title = models.CharField(
			u'Título',
			max_length=100,
		)
	published = models.BooleanField(
			u'Exibido',
			default=True,
		)
	link = models.URLField(
			u'Fonte da notícia',
			max_length=200,
		)
	category = models.ForeignKey(
			Category,
			verbose_name=u'categoria',
			related_name=u'noticia'
		)
	font = models.ForeignKey(
			NewsPortals,
			verbose_name=u'Fonte da notícia',
		)
	# Audit fields
	created_on = models.DateTimeField(
			u'Exibido em',
			auto_now_add=True,
		)

	def __unicode__(self):
		return self.title
=======
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
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
