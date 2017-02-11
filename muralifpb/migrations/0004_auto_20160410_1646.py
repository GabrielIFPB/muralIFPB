# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0003_auto_20160407_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermy',
            name='is_reitoria',
            field=models.BooleanField(default=False, verbose_name=b'\xc3\x89 da reitoria?'),
        ),
        migrations.AlterField(
            model_name='usermy',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=b'\xc3\x89 da equipe administrativa?'),
        ),
    ]
