from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Nombre de categoría")

    def __str__(self):
        return self.nombre

