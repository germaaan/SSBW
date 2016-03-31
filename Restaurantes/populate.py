import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurantes.settings')

import django
django.setup()

from app_restaurantes.models import Restaurante, Plato

def populate():
	res_1 = add_res("Bar de tapas", "Calle Gonzalo Gallas, 1", "bartapas@gmail.com", 0)

	add_plato(res=res_1, nombre="Carne con tomate", precio=2)
	add_plato(res=res_1, nombre="Hamburguesa", precio=1.5)
	add_plato(res=res_1, nombre="Bocadillo de lomo", precio=3)

	res_2 = add_res("Otro bar", "Calle Pedro Antonio de Alarcon, 1", "otrobar@gmail.com", 0)

	add_plato(res=res_2, nombre="Salchichas al vino", precio=1.2)
	add_plato(res=res_2, nombre="Chorizo al infierno", precio=2)
	add_plato(res=res_2, nombre="Alitas de pollo", precio=2.2)

	for r in Restaurante.objects.all():
		for p in Plato.objects.filter(restaurante=r):
			print "- {0} - {1}".format(str(r), str(p))

def add_plato(res, nombre, precio):
	p = Plato.objects.get_or_create(restaurante=res, nombre=nombre, precio=precio, votos=votos)[0]
	p.save()
	return p

def add_res(nombre, direccion, correo):
	r = Restaurante.objects.get_or_create(nombre=nombre, direccion=direccion, correo=correo)[0]
	return r

# Start execution here!
if __name__ == '__main__':
	print("Ejecutando script de poblacion de Restaurantes...")
	populate()
