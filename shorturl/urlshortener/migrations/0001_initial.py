# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('longURL', models.URLField(unique=True)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('date', models.DateTimeField(verbose_name='creation date', auto_now_add=True)),
                ('creator', models.CharField(null=True, max_length=80)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]
