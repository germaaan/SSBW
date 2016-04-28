from django.forms import ModelForm

from django import forms

from app_restaurantes.models import Restaurante, Plato

class RestauranteForm(ModelForm):
	class Meta:
		model = Restaurante
		fields = ['nombre', 'direccion', 'foto', 'votos']


class PlatoForm(ModelForm):
	class Meta:
		model = Plato
		fields = ['nombre', 'precio']
