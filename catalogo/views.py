from django.shortcuts import render

# Create your views here.
from django.httpimportHttpResponse
def inicio(request):
return HttpResponse("Bienvenidoalcatalogo de latienda")
def ofertas(request):
return HttpResponse("Estassonlasofertasdelasemana")