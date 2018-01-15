from django.conf.urls import include,url
from . import views

urlpatterns = [
        url(r'^$', views.users_list, name='inicio'),        
        url(r'^profe/(?P<pk>[0-9]+)/$', views.perfil_profe, name='perfil_profe'),
        url(r'^alumno/(?P<pk>[0-9]+)/$', views.perfil_alumno, name='perfil_alumno'),
    ]