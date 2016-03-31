from django.conf.urls import url
from app_restaurantes import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^votar/', views.votar, name='votar'),
]
