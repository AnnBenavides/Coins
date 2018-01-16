from django.db import models


# Create your models here.
class Profesor(models.Model):
	user = models.ForeignKey('auth.User')
	nombre = user.get_full_name()
	coins_acumuladas = models.IntegerField()
	
	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	user = models.ForeignKey('auth.User')
	nombre = user.get_full_name()
	saldo = models.IntegerField(default=20)
	gastado = models.IntegerField(default=0)
	grupo = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nombre

class Grupo(models.Model):
	nroGrupo = models.IntegerField(primary_key=True)
	usr1 = models.ForeignKey(Alumno)
	usr2 = models.ForeignKey(Alumno)
	usr3 = models.ForeignKey(Alumno)
	usr4 = models.ForeignKey(Alumno)
	usr5 = models.ForeignKey(Alumno,blank=True, null=True)

	def __str__(self):
		return str(self.nroGrupo)








