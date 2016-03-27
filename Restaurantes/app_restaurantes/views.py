from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'mensaje': 'Hola mundo!'}
    return render(request, 'app_restaurantes/base.html', context)

def login(request):
    return HttpResponse("Usuario: " + request.POST.get('usuario') + " Password: " + request.POST.get('password'))
