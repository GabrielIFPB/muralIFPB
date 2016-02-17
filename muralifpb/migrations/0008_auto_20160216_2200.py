# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('muralifpb', '0007_userstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstudent',
            name='email',
            field=models.EmailField(default='jeronimogbariel@gmail.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userstudent',
            name='user',
            field=models.OneToOneField(related_name='Usuarios', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
