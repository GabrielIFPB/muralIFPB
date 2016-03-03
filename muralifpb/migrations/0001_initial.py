# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
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
                ('published', models.BooleanField(default=True, verbose_name='Exibido')),
                ('link', models.URLField(verbose_name='Fonte da not\xedcia')),
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
                ('user', models.OneToOneField(related_name='Usuarios', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(verbose_name='Postado por', to='muralifpb.UserStudent'),
        ),
        migrations.AddField(
            model_name='news',
            name='font',
            field=models.ForeignKey(verbose_name='Fonte da not\xedcia', to='muralifpb.NewsPortals'),
=======
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField()),
                ('birth', models.DateField()),
            ],
>>>>>>> bc8738dda0721983b8b34c685e243768f58c49f0
        ),
    ]
