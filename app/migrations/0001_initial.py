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
                ('name', models.CharField(max_length=60)),
                ('coins', models.IntegerField(default=0)),
                ('gastado', models.IntegerField(default=0)),
                ('grupo', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('idBloque', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(choices=[('21', 'Lunes 21'), ('22', 'Martes 22'), ('23', 'Miercoles 23'), ('24', 'Jueves 24'), ('25', 'Viernes 25')], max_length=2, default='22')),
                ('horas', models.CharField(choices=[('01', '14:00 - 14:15'), ('02', '14:15 - 14:30'), ('03', '14:30 - 14:45'), ('04', '14:45 - 15:00'), ('05', '15:00 - 15:15'), ('06', '15:15 - 15:30'), ('07', '15:30 - 15:45'), ('08', '15:45 - 16:00'), ('09', '16:00 - 16:15'), ('10', '16:15 - 16:30'), ('11', '16:30 - 16:45'), ('12', '16:45 - 17:00'), ('13', '17:00 - 17:15'), ('14', '17:15 - 17:30'), ('15', '17:30 - 17:45'), ('16', '17:45 - 18:00')], max_length=2, default='01')),
                ('valor', models.IntegerField(default=1)),
                ('estado', models.CharField(choices=[('0', 'Ausente'), ('1', 'Presente'), ('2', 'Comprado')], max_length=1, default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('carga', models.IntegerField()),
                ('asunto', models.TextField()),
                ('alumno', models.ForeignKey(to='app.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('nroGrupo', models.IntegerField(primary_key=True, serialize=False)),
                ('usr1', models.ForeignKey(to='app.Alumno', related_name='1+')),
                ('usr2', models.ForeignKey(to='app.Alumno', related_name='2+')),
                ('usr3', models.ForeignKey(to='app.Alumno', related_name='3+')),
                ('usr4', models.ForeignKey(to='app.Alumno', related_name='4+')),
                ('usr5', models.ForeignKey(blank=True, to='app.Alumno', null=True, related_name='5+')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('asunto', models.TextField()),
                ('valor', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=60)),
                ('coins', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carga',
            name='profesor',
            field=models.ForeignKey(to='app.Profesor'),
        ),
        migrations.AddField(
            model_name='bloque',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, to='app.Grupo'),
        ),
        migrations.AddField(
            model_name='bloque',
            name='profe',
            field=models.ForeignKey(to='app.Profesor'),
        ),
    ]
