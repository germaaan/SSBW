from rest_framework import serializers
from app_restaurantes.models import Restaurante, Plato

class RestauranteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurante
		fields = ("nombre", "direccion", "votos",)

class PlatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plato
		fields = ("nombre", "precio", "restaurante")
