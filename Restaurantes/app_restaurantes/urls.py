from django.conf.urls import url
from app_restaurantes import views
from app_restaurantes.views import *

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^votar/', views.votar, name='votar'),
    url(r'^api/restaurantes$', views.api_restaurantes, name='api_restaurantes'),
    url(r'^api/platos$', views.api_platos, name='api_platos'),
    #url(r'^api/v1/restaurantes/$', 'restaurante_coleccion'),
    #url(r'^api/v1/restaurantes/(?P<pk>[0-9]+)$', 'restaurante_elemento')
]
