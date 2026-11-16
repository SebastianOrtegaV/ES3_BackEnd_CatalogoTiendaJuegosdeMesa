from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'email', 'telefono', 'cantidad']

    def __init__(self, *args, juego, **kwargs):
        super().__init__(*args, **kwargs)
        self.juego = juego

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1 or cantidad > 5:
            raise forms.ValidationError('La cantidad debe estar entre 1 y 5.')
        if self.juego.stock <= 0:
            raise forms.ValidationError('Este juego está agotado.')
        if cantidad > self.juego.stock:
            raise forms.ValidationError(
                f'Solo quedan {self.juego.stock} unidades disponibles.')
        return cantidad