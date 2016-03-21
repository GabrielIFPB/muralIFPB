# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0004_auto_20160315_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=b'2016-03-20 00:00', verbose_name='Publicado em'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='Postado por', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
