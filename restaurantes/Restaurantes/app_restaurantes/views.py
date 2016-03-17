from django.http import HttpResponse

def otra_funcion (request):
    return HttpResponse("Hola mundo")


from django.shortcuts import render           # para plantillas
def index (request)
	context= {
		'mensaje': 'hola mundo',
	}
	return render (request, 'base.html', context)
