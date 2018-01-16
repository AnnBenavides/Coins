from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profesor(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=60)
	coins = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name

	def cargar(self, carga):
		self.coins = self.coins + carga
		self.save()

class Alumno(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=60)
	coins = models.IntegerField(default=0)
	gastado = models.IntegerField(default=0)
	grupo = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name

	def cargar(self, carga):
		self.coins = self.coins + carga
		self.save()

	def gastar(self, gasto):
		self.coins = self.coins - gasto
		self.gastado = self.gastado + gasto
		self.save()

class Grupo(models.Model):
	nroGrupo = models.IntegerField(primary_key=True)
	usr1 = models.ForeignKey(Alumno, related_name='1+')
	usr2 = models.ForeignKey(Alumno, related_name='2+')
	usr3 = models.ForeignKey(Alumno, related_name='3+')
	usr4 = models.ForeignKey(Alumno, related_name='4+')
	usr5 = models.ForeignKey(Alumno, related_name='5+',blank=True, null=True)

	def __str__(self):
		return str(self.nroGrupo)

class Bloque(models.Model):
	idBloque = models.AutoField(primary_key=True)
	profe = models.ForeignKey(Profesor)
	DIAS_CHOICES = (("21","Lunes"),
			("22","Martes"),
			("23","Miercoles"),
			("24","Jueves"),
			("25","Viernes"),
			)
	HORAS_CHOICES = (
			("01","14:00 - 14:15"),
			("02","14:15 - 14:30"),
			("03","14:30 - 14:45"),
			("04","14:45 - 15:00"),
			("05","15:00 - 15:15"),
			("06","15:15 - 15:30"),
			("07","15:30 - 15:45"),
			("08","15:45 - 16:00"),
			("09","16:00 - 16:15"),
			("10","16:15 - 16:30"),
			("11","16:30 - 16:45"),
			("12","16:45 - 17:00"),
			("13","17:00 - 17:15"),
			("14","17:15 - 17:30"),
			("15","17:30 - 17:45"),
			("16","17:45 - 18:00"),
			)
	dia = models.CharField(max_length=2,choices=DIAS_CHOICES, default="22")
	horas = models.CharField(max_length=2,choices=HORAS_CHOICES, default="01")
	valor = models.IntegerField(default=1)
	ESTADOS_CHOICES = (("0","Ausente"),("1","Presente"),("2","Comprado"),)
	estado = models.CharField(max_length=1,choices=ESTADOS_CHOICES, default="0")
	grupo = models.ForeignKey(Grupo, blank=True, null=True)

	def __str__(self):
		return str(self.profe)+": "+self.dia+" "+self.horas

	def ausente(self):
		self.estado = "0"
		self.save()

	def presente(self, coins):
		self.estado = "1"
		self.valor = coins
		self.save()

	def comprado(self, nroGrupo):
		self.estado = "2"
		self.grupo = nroGrupo
		self.profe.cargar(self.valor)
		self.save()

class Bien(models.Model):
	nombre = models.CharField(max_length=50)
	valor = models.IntegerField(default=1)

	def __str__(self):
		return self.nombre+": "+str(self.valor)

class Historial(models.Model):
	user = models.ForeignKey(User)
	asunto = models.TextField()
	valor = models.IntegerField()
	date = timezone.now()

	def __str__(self):
		return str(self.user)+" | "+ self.asunto







