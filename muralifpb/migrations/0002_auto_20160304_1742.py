# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='Postado por', blank=True, to='muralifpb.UserStudent', null=True),
        ),
    ]
