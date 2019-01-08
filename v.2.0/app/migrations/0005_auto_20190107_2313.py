# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190107_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='taller',
        ),
        migrations.AlterField(
            model_name='profesor',
            name='taller',
            field=models.CharField(null=True, max_length=130),
        ),
        migrations.DeleteModel(
            name='Taller',
        ),
    ]
