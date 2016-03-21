# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserStudent(models.Model):

	matricula = models.CharField(
			verbose_name='Matricula',
			max_length=30,
			unique=True,
			null=False,
			blank=False,
		)
	email = models.EmailField(
			verbose_name='Email',
			max_length=200,
			unique=True,
			null=False,
			blank=False,
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
			null=False,
			blank=False,
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

	def __unicode__(self):
		return self.name

class PublishedManager(models.Manager):

	def get_query_set(self):
		return super(PublishedManager, self).get_query_set().filter(published=True)

class UnpublishedManager(models.Manager):

	def get_query_set(self):
		return super(UnpublishedManager, self).get_query_set().filter(published=False)

class Post(models.Model):

	class Meta:
		verbose_name = u'Post'
		verbose_name_plural = u'Posts'
		#ordena do mais novo para o mais antigo
		ordering = [u'created_on']
		#ordena do mais antigo para o mais novo
		#ordering = [u'-created_on']

	author = models.ForeignKey(
			User,
			verbose_name=u'Postado por',
			null=True,
			blank=True,
		)
	title = models.CharField(
			u'Título',
			max_length=100,
			null=False,
			blank=False,
		)
	text = models.TextField(
			u'Texto',
			null=False,
			blank=False,
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

	objects = models.Manager()
	published_objects = PublishedManager()
	unpublished_objects = UnpublishedManager()

	def __unicode__(self):
		return self.title

class NewsPortals(models.Model):

	name = models.CharField(
			u'Nome do protal de notícia',
			max_length=100,
			null=False,
			blank=False,
		)
	link = models.URLField(
			u'Fonte da notícia',
			max_length=200,
			null=False,
			blank=False,
		)

	def __unicode__(self):
		return self.name

class News(models.Model):

	class Meta:
		verbose_name = u'Notícia'
		verbose_name_plural = u'Notícias'

	category = models.ForeignKey(
			Category,
			verbose_name=u'categoria',
			related_name=u'noticia'
		)
	font = models.ForeignKey(
			NewsPortals,
			verbose_name=u'Fonte da notícia',
		)
	title = models.CharField(
			u'Título',
			max_length=100,
			null=False,
			blank=False,
		)
	text = models.TextField(
			u'Texto',
			null=False,
			blank=False,
			default=''
		)
	link = models.URLField(
			u'Fonte da notícia',
			max_length=200,
			null=False,
			blank=False,
		)
	published_date = models.DateTimeField(
			u'Publicado em',
			
		)
	published = models.BooleanField(
			u'Exibido',
			default=False,
		)
	# Audit fields
	created_on = models.DateTimeField(
			u'Exibido em',
			auto_now_add=True,
		)

	@staticmethod
	def creating_news(link=None):
		#BeautifulSoup
		#requests
		if link is not None:
			feeds = feedparser.parse(link)

			for feed in feeds['entries']:
				news = News(
						title=feed.title,
						text=feed.content[0].value,
						link=feed.link,
						published_date=feed.date
					)
				news.save()
			return True
		else:
			raise ValidationError(u'O link não pode se None!')
			return False

	def __unicode__(self):
		return self.title