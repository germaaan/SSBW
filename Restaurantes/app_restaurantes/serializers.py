from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, generics
from app_restaurantes.models import Restaurante, Plato

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class RestauranteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurante
		fields = ['nombre', 'direccion', 'foto', 'votos', 'slug']

class PlatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plato
		fields = ['restaurante', 'nombre', 'precio']
