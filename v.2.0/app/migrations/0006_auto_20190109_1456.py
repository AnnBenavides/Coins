# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190107_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='asunto',
            field=models.CharField(max_length=70, blank=True, null=True),
        ),
    ]
