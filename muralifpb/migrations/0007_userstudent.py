# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muralifpb', '0006_auto_20160215_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.CharField(unique=True, max_length=10)),
                ('user', models.OneToOneField(verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
