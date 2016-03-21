# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0003_auto_20160315_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=b'2016-03-15 00:00', verbose_name='Publicado em'),
        ),
    ]
