from django.shortcuts import render, redirect
from .forms import (
    ProductoForm, ClienteForm, VentaForm, BuscarProductoForm
)
from .models import Producto

def index(request):
    return render(request, 'myapp/index.html')

def agregar_producto(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'myapp/form_generic.html', {
        'titulo': 'Agregar Producto',
        'form': form
    })

def agregar_cliente(request):
    form = ClienteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'myapp/form_generic.html', {
        'titulo': 'Agregar Cliente',
        'form': form
    })

def agregar_venta(request):
    form = VentaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'myapp/form_generic.html', {
        'titulo': 'Registrar Venta',
        'form': form
    })

def buscar_producto(request):
    resultados = None
    form = BuscarProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        q = form.cleaned_data['nombre']
        resultados = Producto.objects.filter(nombre__icontains=q)
    return render(request, 'myapp/buscar.html', {
        'form': form,
        'resultados': resultados
    })
