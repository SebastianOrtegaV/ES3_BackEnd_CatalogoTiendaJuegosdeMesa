from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Nombre de categoría")

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='juegos',
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=120, verbose_name="Nombre del juego")
    precio = models.PositiveIntegerField(verbose_name="Precio en pesos ($)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock en bodega")
    disponible = models.BooleanField(default=True, verbose_name="Disponible para la venta")

    def __str__(self):
        return f"{self.nombre} (${self.precio})"