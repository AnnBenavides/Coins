# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190109_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='group',
            field=models.ForeignKey(on_delete='PROTECT', to='app.Grupo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bloque',
            name='grupo',
            field=models.ForeignKey(on_delete='PROTECT', to='app.Grupo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloque',
            name='profe',
            field=models.ForeignKey(on_delete='PROTECT', to='app.Profesor'),
        ),
        migrations.AlterField(
            model_name='carga',
            name='alumno',
            field=models.ForeignKey(on_delete='PROTECT', to='app.Alumno'),
        ),
        migrations.AlterField(
            model_name='carga',
            name='profesor',
            field=models.ForeignKey(on_delete='PROTECT', to='app.Profesor'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='user',
            field=models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user',
            field=models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL),
        ),
    ]
