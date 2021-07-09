from django.shortcuts import render
from .models import Enlace
from django.http import HttpResponse

def Enlaces(request):
    
    enlace = Enlace.objects.all()
    return render(request, 'links/enlaces.html', {'enlaces': enlace})