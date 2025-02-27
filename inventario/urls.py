from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('cliente/dispositivos/', views.cliente_dispositivos, name='cliente_dispositivos'),
    path('cliente/dispositivos/<int:dispositivo_id>/caracteristicas/', views.cliente_caracteristicas, name='cliente_caracteristicas'),
]