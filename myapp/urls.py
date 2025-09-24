from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
