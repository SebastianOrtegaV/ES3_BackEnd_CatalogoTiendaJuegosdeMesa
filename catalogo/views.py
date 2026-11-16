from django.shortcuts import render
from .models import Categoria, Juego
from django.http import HttpResponse 

def inicio(request):
    juegos = Juego.objects.select_related("categoria").filter(disponible=True)
    return render(request, "catalogo/inicio.html", {"juegos": juegos})

def ofertas(request):
    return HttpResponse("Estassonlasofertasdelasemana") 