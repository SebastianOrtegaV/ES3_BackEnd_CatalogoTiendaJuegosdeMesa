from django.contrib import admin
from .models import Categoria, Juego
from django.utils.html import format_html


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion', 'precio', 'precio_formateado', 'stock', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)
    list_editable = ('precio', 'stock', 'disponible')

    @admin.display(description='Juego - Precio Formateado', ordering='precio')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen.url)
        return "No hay imagen"
    
    def precio_formateado(self, obj):
        return f"$ {obj.precio:,}".replace(",", ".")