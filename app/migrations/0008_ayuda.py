# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190110_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayuda',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('costo', models.IntegerField(default=2)),
                ('comprador', models.ForeignKey(to='app.Alumno', related_name='comprador')),
                ('servidor', models.ForeignKey(to='app.Alumno', related_name='servidor')),
            ],
        ),
    ]
