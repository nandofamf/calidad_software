from django.urls import path
from tienda import views

urlpatterns = [
    # Ruta para la página de inicio
    path('', views.index, name='index'),
    
    # Ruta para la página de contacto
    path('contacto/', views.contacto, name='contacto'),
    
    # Ruta para la página del carrito
    path('carrito/', views.carrito, name='carrito'),
    
    # Rutas para los productos
    path('producto1/', views.producto1, name='producto1'),
    path('producto2/', views.producto2, name='producto2'),
    path('producto3/', views.producto3, name='producto3'),
    path('producto4/', views.producto4, name='producto4'),
    path('producto5/', views.producto5, name='producto5'),
    path('producto6/', views.producto6, name='producto6'),
]
