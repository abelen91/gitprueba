# gitprueba
# Proyecto Django Nuñez Ana Belén- Mi Tienda

## Cómo correr
1. Crear venv e instalar dependencias (Django 4+).
2. `python manage.py migrate`
3. (Opcional) `python manage.py createsuperuser`
4. `python manage.py runserver` y abrir `http://127.0.0.1:8000/`

## Funcionalidades
- **Herencia de plantillas**: `base.html` con `{% block content %}`. Páginas que heredan: `index.html`, `form_generic.html`, `buscar.html`.
- **Modelos (3 clases)**: `Producto`, `Cliente`, `Venta`.
- **Formularios de alta**: `/producto/nuevo/`, `/cliente/nuevo/`, `/venta/nueva/`.
- **Formulario de búsqueda**: `/buscar/` (por nombre de producto).
- **Admin**: `/admin/` (si creaste superusuario).

## Orden sugerido para probar
1. Crear Productos y Clientes.
2. Registrar una Venta.
3. Buscar Productos por nombre.
