from django.shortcuts import render, get_object_or_404
from .models import Juego, Categoria

def lista_juegos(request):
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q', '')

    juegos = Juego.objects.select_related('categoria').filter(disponible=True)

    if categoria_id:
        juegos = juegos.filter(categoria_id=categoria_id)
    if busqueda:
        juegos = juegos.filter(nombre__icontains=busqueda)

    context = {
        'juegos': juegos,
        'categorias': Categoria.objects.all(),
        'busqueda_actual': busqueda,
        'categoria_actual': categoria_id,
    }
    return render(request, 'catalogo/index.html', context)

def detalle_juego(request, pk):
    juego = get_object_or_404(
        Juego.objects.select_related('categoria'),
        pk=pk, disponible=True)
    return render(request, 'catalogo/detalle.html', {'juego': juego})