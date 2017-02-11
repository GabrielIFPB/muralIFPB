# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserStudent',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='Postado por', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
