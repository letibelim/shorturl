# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_auto_20170115_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='creator',
            field=models.CharField(max_length=80, blank=True, null=True),
        ),
    ]
