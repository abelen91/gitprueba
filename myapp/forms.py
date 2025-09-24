from django import forms
from .models import Producto, Cliente, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto", max_length=100)
