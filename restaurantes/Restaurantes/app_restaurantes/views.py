from django.http import HttpResponse
from django.shortcuts import render

def otra_funcion (request):
    return HttpResponse("Hola mundo")

def index (request):
	context= {
		'mensaje': 'hola mundo',
	}
	return render(request, "app_restaurantes/base.html", context)
