from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_restaurantes.models import Restaurante, Plato
from app_restaurantes.serializers import RestauranteSerializer, PlatoSerializer

def index(request):
    r = Restaurante.objects.all()
    context = {'mensaje': 'Hola mundo!', 'restaurantes': r[:4]}
    return render(request, 'app_restaurantes/base.html', context)

def login(request):
    return HttpResponse("Usuario: " + request.POST.get('usuario') + " Password: " + request.POST.get('password'))

def votar(request):
    r = Restaurante.objects.get(nombre=request.GET.get('restaurante'))
    r.votos = r.votos + 1
    r.save()

    return JsonResponse({'votos':r.votos})

@api_view(['GET'])
def restaurante_coleccion(request):
    if request.method == 'GET':
        restaurantes = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurantes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def restaurante_elemento(request, pk):
    try:
        restaurante = Restaurante.objects.get(pk=pk)
    except Restaurante.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestauranteSerializer(post)
        return Response(serializer.data)
