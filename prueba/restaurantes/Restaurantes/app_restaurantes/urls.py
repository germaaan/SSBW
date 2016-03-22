from django.conf.urls import url
from app_restaurantes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
