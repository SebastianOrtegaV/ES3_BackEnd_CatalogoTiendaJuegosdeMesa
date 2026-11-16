from django.db import models
import uuid

def formato_pesos(valor):
    return f"${valor:,}".replace(',', '.')

def generar_codigo():
    return "PED-" + uuid.uuid4().hex[:8].upper()


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
    imagen = models.ImageField(
        upload_to='juegos/', 
        blank=True, 
        null=True, 
        verbose_name="Imagen de la caja"
    )
    def __str__(self):
        return self.nombre
    @property
    def precio_clp(self):
        return formato_pesos(self.precio)

class Pedido(models.Model):
    juego = models.ForeignKey(
        Juego,
        on_delete=models.CASCADE,
        related_name='pedidos',
    )
    nombre = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='correo')
    telefono = models.CharField(max_length=15, verbose_name='teléfono')
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=12, unique=True,
                              default=generar_codigo, editable=False)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"