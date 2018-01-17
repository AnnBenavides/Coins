from django.contrib import admin
from .models import Alumno, Grupo, Profesor, Bloque, Bien, Historial


# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(Bloque)
admin.site.register(Bien)
admin.site.register(Historial)