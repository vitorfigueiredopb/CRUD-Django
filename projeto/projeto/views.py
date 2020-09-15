from django.http import HttpResponse
from django.shortcuts import render

def lista_consoles(request):
    return render(request, 'lista_consoles.html')