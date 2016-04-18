from django.conf.urls import url
from app_restaurantes import views
from app_restaurantes.views import *

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logup/', views.logup, name='logup'),
    url(r'^votar/', views.votar, name='votar'),
    url(r'^api/v1/restaurantes/$', 'restaurante_coleccion'),
    url(r'^api/v1/restaurantes/(?P<pk>[0-9]+)$', 'restaurante_elemento')
]
