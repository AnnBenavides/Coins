# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('saldo', models.IntegerField(default=20)),
                ('gastado', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('nroGrupo', models.AutoField(primary_key=True, serialize=False)),
                ('computacion', models.ForeignKey(related_name='computacion', to='app.Alumno')),
                ('diseno', models.ForeignKey(related_name='diseno', to='app.Alumno')),
                ('modelamiento', models.ForeignKey(related_name='modelamiento', to='app.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('coins_acumuladas', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=25)),
                ('profesor', models.ForeignKey(to='app.Profesor')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='taller',
            field=models.ForeignKey(to='app.Taller'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
