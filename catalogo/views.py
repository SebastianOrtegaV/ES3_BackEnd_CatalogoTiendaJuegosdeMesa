from django.shortcuts import render, get_object_or_404
from .models import Juego, Categoria

def lista_juegos(request):
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q', '')

    juegos = Juego.objects.all()
    
    if categoria_id:
        juegos = juegos.filter(categoria_id=categoria_id)
    if busqueda:
        juegos = juegos.filter(nombre__icontains=busqueda)

    categorias = Categoria.objects.all()

    context = {
        'juegos': juegos,
        'categorias': categorias,
        'busqueda_actual': busqueda,
    }
    return render(request, 'catalogo/index.html', context)

def detalle_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    return render(request, 'catalogo/detalle.html', {'juego': juego})