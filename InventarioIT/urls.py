from django.contrib import admin
from django.urls import path, include
from auth.views import AdminRedirectView

urlpatterns = [
    path('admin/', AdminRedirectView.as_view(), name='admin'),
    path('', include('auth.urls', namespace='auth')),  # Rutas de autenticación
    path('', include('inventario.urls', namespace='inventario')),  # Rutas de inventario
]