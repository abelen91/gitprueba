from django.shortcuts import render
from .models import Producto
from .forms import BuscarProductoForm

def buscar_producto(request):
    form = BuscarProductoForm(request.GET or None)
    productos = []

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)

    return render(request, 'myapp/buscar.html', {'form': form, 'productos': productos})
