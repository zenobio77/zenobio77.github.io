from django.shortcuts import render
from .models import Image


def paginaPrincipal(request):
    context = {'logo': Image.objects.get(name='logo')}
    return render(request, 'landingpages/paginaPrincipal.html', context)

def quemSomos(request):
    context = {
        'title': 'Quem somos',
        'logo': Image.objects.get(name='logo'),
        'quemSomos': Image.objects.get(name='quemSomos')
    }
    return render(request, 'landingpages/quemSomos.html', context)

def servicos(request):
    context = {
        'title': 'Servicos',
        'logo': Image.objects.get(name='logo'),
        'iconUpload': Image.objects.get(name='iconUpload'),
        'iconDownload': Image.objects.get(name='iconDownload'),
        'iconWork': Image.objects.get(name='iconWork')
    }
    return render(request, 'landingpages/servicos.html', context)
