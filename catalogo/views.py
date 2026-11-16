from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Juego, Categoria
from .forms import PedidoForm

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

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.juego = juego
            pedido.save()
            messages.success(request, 'Pedido registrado.')
            return redirect('catalogo:detalle_juego', pk=juego.pk)
    else:
        form = PedidoForm()

    return render(request, 'catalogo/detalle.html', {'juego': juego, 'form': form})