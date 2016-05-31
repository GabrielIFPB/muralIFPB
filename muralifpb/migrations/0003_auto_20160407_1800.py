# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0002_auto_20160406_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermy',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'imagem', blank=True),
        ),
        migrations.AddField(
            model_name='usermy',
            name='matricula',
            field=models.CharField(default='', unique=True, max_length=30, verbose_name=b'Matricula'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermy',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Nome de Usu\xc3\xa1rio', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), b'O nome de usu\xc3\xa1rio s\xc3\xb3 pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', b'invalid')]),
        ),
    ]
