# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180118_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=130)),
            ],
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='coins',
            new_name='coins_remain',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='gastado',
            new_name='coins_used',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='grupo',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='coins',
            new_name='coins_collected',
        ),
        migrations.AlterField(
            model_name='bloque',
            name='dia',
            field=models.CharField(choices=[('14', 'Lunes 14'), ('15', 'Martes 15'), ('16', 'Miercoles 16'), ('17', 'Jueves 17'), ('18', 'Viernes 18')], max_length=2, default='14'),
        ),
        migrations.AlterField(
            model_name='bloque',
            name='horas',
            field=models.CharField(choices=[('01', '14:00 - 14:15'), ('02', '14:15 - 14:30'), ('03', '14:30 - 14:45'), ('04', '14:45 - 15:00'), ('05', '15:00 - 15:15'), ('06', '15:15 - 15:30'), ('07', '15:30 - 15:45'), ('08', '15:45 - 16:00'), ('09', '16:00 - 16:15'), ('10', '16:15 - 16:30'), ('11', '16:30 - 16:45'), ('12', '16:45 - 17:00'), ('13', '17:00 - 17:15'), ('14', '17:15 - 17:30')], max_length=2, default='01'),
        ),
        migrations.AlterField(
            model_name='carga',
            name='asunto',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumno',
            name='taller',
            field=models.ForeignKey(null=True, to='app.Taller'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='taller',
            field=models.ForeignKey(null=True, to='app.Taller'),
        ),
    ]
