# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0002_auto_20160108_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(to='muralifpb.Post'),
        ),
    ]
