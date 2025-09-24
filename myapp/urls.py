from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/nuevo/', views.agregar_producto, name='agregar_producto'),
    path('cliente/nuevo/', views.agregar_cliente, name='agregar_cliente'),
    path('venta/nueva/', views.agregar_venta, name='agregar_venta'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
