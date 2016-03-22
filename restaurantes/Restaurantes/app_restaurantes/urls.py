from django.conf.urls import url
from . import views

urlpatterns = [
    # para /app_restaurantes/index
    url(r'^index$', views.index, name='index'),

    # para /app_restaurantes/otro_url
    url(r'^otro_url$', views.otra_funcion, name='otra_funcion'),
]
