from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('mis-dispositivos/', views.cliente_dispositivos, name='cliente_dispositivos'),
]