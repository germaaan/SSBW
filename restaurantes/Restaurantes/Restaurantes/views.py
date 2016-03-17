from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def index (request):

	return HttpResponse ('hola mundo')


def hola_mundo (request, visitante):
	context = {'visitante': visitante}
	return render (request, 'base.html', context)
