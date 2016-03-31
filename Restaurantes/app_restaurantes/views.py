from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app_restaurantes.models import Restaurante, Plato

def index(request):
    context = {'mensaje': 'Hola mundo!'}
    return render(request, 'app_restaurantes/base.html', context)

def login(request):
    return HttpResponse("Usuario: " + request.POST.get('usuario') + " Password: " + request.POST.get('password'))

def votar(request):
    r = Restaurante.objects.get(nombre=request.GET.get('restaurante'))
    r.votos = r.votos + 1
    r.save()

    return JsonResponse({'votos':r.votos})
