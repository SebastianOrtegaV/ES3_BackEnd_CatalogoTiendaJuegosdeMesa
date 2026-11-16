from django.contrib import admin
from .models import Categoria, Juego

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_formateado', 'stock', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)
    list_editable = ('stock', 'disponible')

    @admin.display(description='Precio', ordering='precio')
    def precio_formateado(self, obj):
        return f"$ {obj.precio:,}".replace(",", ".")