# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_grupo_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='usr1',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='usr2',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='usr3',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='usr4',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='usr5',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='grupo',
            field=models.ForeignKey(to='app.Grupo', null=True, blank=True),
        ),
    ]
