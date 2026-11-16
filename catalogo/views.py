from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Juego, Categoria, Pedido
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
        pk=pk, disponible=True
    )

    if request.method == 'POST':
        form = PedidoForm(request.POST, juego=juego)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.juego = juego
            pedido.save()
            juego.stock -= pedido.cantidad
            juego.save()
            # Redirige al comprobante usando el código único del pedido (Paso 12.2)
            return redirect('catalogo:comprobante', codigo=pedido.codigo)
    else:
        form = PedidoForm(juego=juego)

    return render(request, 'catalogo/detalle.html', {'juego': juego, 'form': form})

def comprobante(request, codigo):
    pedido = get_object_or_404(Pedido.objects.select_related('juego'), codigo=codigo)
    return render(request, 'catalogo/comprobante.html', {'pedido': pedido})