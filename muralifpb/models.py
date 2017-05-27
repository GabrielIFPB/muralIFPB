# -*- coding: UTF-8 -*-
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.utils.translation import ugettext_lazy as _

import re

class UserMy(AbstractBaseUser, PermissionsMixin):

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

	matricula = models.CharField(
			'Matricula',
			unique=True,
			max_length=30,
			null=False,
			blank=False,
		)
	username = models.CharField(
		'Nome de Usuário',
		max_length=30,
		unique=True, 
		validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
			'O nome de usuário só pode conter letras, digitos ou os '
			'seguintes caracteres: @/./+/-/_', 'invalid')]
	)
	email = models.EmailField(
			'Email',
			unique=True,
		)
	image = models.ImageField(
			'imagem',
			null=True,
			blank=True,
		)
	name = models.CharField(
			'Nome',
			max_length=60,
			blank=True,
		)
	is_reitoria = models.BooleanField(
			'É da reitoria?',
			blank=True,
			default=False,
		)
	is_active = models.BooleanField(
			'Está ativo?',
			blank=True,
			default=True,
		)
	is_staff = models.BooleanField(
			'É da equipe administrativa?',
			blank=True,
			default=False,
		)
	date_joined = models.DateTimeField(
			'Data de Entrada',
			auto_now_add=True,
		)

	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return  self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)
		
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

	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(published=True)

class UnpublishedManager(models.Manager):

	def get_queryset(self):
		return super(UnpublishedManager, self).get_queryset().filter(published=False)

class Post(models.Model):

	class Meta:
		verbose_name = u'Post'
		verbose_name_plural = u'Posts'
		#ordena do mais novo para o mais antigo
		ordering = [u'created_on']
		#ordena do mais antigo para o mais novo
		#ordering = [u'-created_on']

	author = models.ForeignKey(
			UserMy,
			verbose_name=u'Postado por',
			null=True,
			blank=True,
		)
	image = models.ImageField(
			upload_to='images',
			verbose_name='imagem',
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
			u'Nome do portal de notícia',
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
	def creating_news():
		#BeautifulSoup
		#requests
		portais = NewsPortals.objects.all()
		if portais is not None:
			for portal in portais:
				feeds = feedparser.parse(portal.link)

				for feed in feeds['entries']:
					news = News(
							title=feed.title,
							text=feed.content[0].value,
							link=feed.link,
							published_date=feed.date
						)
					news.save()
		else:
			raise ValidationError(u'O link não pode se None!')

	def __unicode__(self):
		return self.title