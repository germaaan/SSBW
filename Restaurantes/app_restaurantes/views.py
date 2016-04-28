from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, generics
from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.template.defaultfilters import slugify

from app_restaurantes.models import Restaurante, Plato
from app_restaurantes.forms import RestauranteForm, PlatoForm
from app_restaurantes.serializers import RestauranteSerializer, PlatoSerializer

def index(request):
    r = Restaurante.objects.all()
    context = {'mensaje': 'Hola mundo!', 'restaurantes': r[:4]}
    return render(request, 'base.html', context)

def votar(request):
    r = Restaurante.objects.get(nombre=request.GET.get('restaurante'))
    r.votos = r.votos + 1
    r.save()

    return JsonResponse({'votos':r.votos})

@api_view(['GET'])
def api_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    result = RestauranteSerializer(restaurantes, many=True)
    return Response(result.data)

@api_view(['GET'])
def api_platos(request):
    platos = Plato.objects.all()
    result = PlatoSerializer(platos, many=True)
    return Response(result.data)

# @api_view(['GET'])
# def restaurante_coleccion(request):
    # if request.method == 'GET':
        # restaurantes = Restaurante.objects.all()
        # serializer = RestauranteSerializer(restaurantes, many=True)
        # return Response(serializer.data)

# @api_view(['GET'])
# def restaurante_elemento(request, pk):
    # try:
        # restaurante = Restaurante.objects.get(pk=pk)
    # except Restaurante.DoesNotExist:
        # return HttpResponse(status=404)

    # if request.method == 'GET':
        # serializer = RestauranteSerializer(post)
        # return Response(serializer.data)
