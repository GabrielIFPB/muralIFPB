# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0002_auto_20160304_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=b'2016-03-15 00:00', verbose_name='Publicado em'),
        ),
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.TextField(default=b'', verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Exibido'),
        ),
    ]
