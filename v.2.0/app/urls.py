from django.conf.urls import include,url
from . import views

urlpatterns = [
        url(r'^$', views.users_list, name='inicio'),        
        url(r'^profe/(?P<pk>[0-9]+)/$', views.perfil_profe, name='perfil_profe'),
        url(r'^alumno/(?P<pk>[0-9]+)/$', views.perfil_alumno, name='perfil_alumno'),
        url(r'^alumno/(?P<pk>[0-9]+)/ayuda/$', views.ayuda, name='ayuda'),
        url(r'^bien/(?P<pk>[0-9]+)$', views.bien, name='bien'),
        url(r'^bien/nuevo/$', views.nuevo_bien, name='nuevo_bien'),
        url(r'^horario/nuevo/$', views.nuevo_bloque, name='nuevo_bloque'),
        url(r'^horario/(?P<pk>[0-9]+)$', views.editar_bloque, name='editar_bloque'),
        url(r'^horario/comprar/(?P<pk>[0-9]+)$', views.comprar_bloque, name='comprar_bloque'),
        url(r'^horario/borrar/(?P<pk>[0-9]+)$', views.borrar_bloque, name='borrar_bloque'),
        url(r'^cargar/$', views.cargar_coins, name='cargar_coins'),
    ]