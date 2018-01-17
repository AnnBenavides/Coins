# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('carga', models.IntegerField()),
                ('asunto', models.TextField()),
                ('alumno', models.ForeignKey(to='app.Alumno')),
                ('profesor', models.ForeignKey(to='app.Profesor')),
            ],
        ),
        migrations.AlterField(
            model_name='bloque',
            name='dia',
            field=models.CharField(default='22', max_length=2, choices=[('21', 'Lunes 21'), ('22', 'Martes 22'), ('23', 'Miercoles 23'), ('24', 'Jueves 24'), ('25', 'Viernes 25')]),
        ),
    ]
