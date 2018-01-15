# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='taller',
            field=models.ForeignKey(blank=True, to='app.Taller'),
        ),
    ]
