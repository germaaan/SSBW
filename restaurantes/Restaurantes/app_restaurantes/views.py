from django.http import HttpResponse
def otra_funcion (request):
    return HttpResponse("Hola mundo")

from django.shortcuts import render
def index (request):
	context= {
		'mensaje': 'hola mundo',
	}

	return render (request, 'base.html', context)
