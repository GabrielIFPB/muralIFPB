# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=40, verbose_name=b'Nome de Usu\xc3\xa1rio')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'Email')),
                ('name', models.CharField(max_length=60, verbose_name=b'Nome', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Est\xc3\xa1 ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'\xc3\x89 da equipe?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de Entrada')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('text', models.TextField(default=b'', verbose_name='Texto')),
                ('link', models.URLField(verbose_name='Fonte da not\xedcia')),
                ('published_date', models.DateTimeField(verbose_name='Publicado em')),
                ('published', models.BooleanField(default=False, verbose_name='Exibido')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Exibido em')),
                ('category', models.ForeignKey(related_name='noticia', verbose_name='categoria', to='muralifpb.Category')),
            ],
            options={
                'verbose_name': 'Not\xedcia',
                'verbose_name_plural': 'Not\xedcias',
            },
        ),
        migrations.CreateModel(
            name='NewsPortals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome do protal de not\xedcia')),
                ('link', models.URLField(verbose_name='Fonte da not\xedcia')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images', null=True, verbose_name=b'imagem', blank=True)),
                ('title', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('text', models.TextField(verbose_name='Texto')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('category', models.ForeignKey(related_name='posts', verbose_name='categoria', to='muralifpb.Category')),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='UserStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.CharField(unique=True, max_length=30, verbose_name=b'Matricula')),
                ('email', models.EmailField(unique=True, max_length=200, verbose_name=b'Email')),
                ('image', models.ImageField(upload_to=b'images', null=True, verbose_name=b'imagem', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='font',
            field=models.ForeignKey(verbose_name='Fonte da not\xedcia', to='muralifpb.NewsPortals'),
        ),
    ]
