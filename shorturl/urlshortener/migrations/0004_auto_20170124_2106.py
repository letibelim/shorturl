# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_auto_20170121_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='code',
            field=models.CharField(max_length=10, blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='longURL',
            field=models.URLField(verbose_name='url to be shortened'),
        ),
    ]
