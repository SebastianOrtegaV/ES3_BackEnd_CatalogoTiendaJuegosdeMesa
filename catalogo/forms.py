from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'email', 'telefono', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1 or cantidad > 5:
            raise forms.ValidationError('La cantidad debe estar entre 1 y 5.')
        return cantidad