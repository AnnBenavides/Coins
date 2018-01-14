from django.db import models

# Create your models here.
class Profesor(models.Model):
	user = models.ForeignKey('auth.User')
	coins_acumuladas = models.IntegerField()
	
	def __str__(self):
		return self.user.get_username()

class Taller(models.Model):
	nombre = models.CharField(max_length=25)
	profesor = models.ForeignKey(Profesor)

	def getTaller(self):
		return self.nombre

	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	user = models.ForeignKey('auth.User')
	saldo = models.IntegerField(default=20)
	gastado = models.IntegerField(default=0)
	taller = models.ForeignKey(Taller)

	def __str__(self):
		return self.user.get_username()

class Grupo(models.Model):
	nroGrupo = models.AutoField(primary_key=True)
	diseno = models.ForeignKey(Alumno, related_name='diseno')
	modelamiento = models.ForeignKey(Alumno, related_name='modelamiento')
	computacion = models.ForeignKey(Alumno, related_name='computacion')

	def __str__(self):
		return str(self.nroGrupo)








