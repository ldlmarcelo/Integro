from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('cliente/dispositivos/', views.ClienteDispositivosView.as_view(), name='cliente_dispositivos'),
    path('cliente/dispositivos/<int:dispositivo_id>/caracteristicas/', views.ClienteCaracteristicasView.as_view(), name='cliente_caracteristicas'),
]