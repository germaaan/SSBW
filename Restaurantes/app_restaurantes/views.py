from django.shortcuts import render

def index(request):
    context = {'mensaje': 'Hola mundo!'}
    return render(request, 'app_restaurantes/base.html', context)
