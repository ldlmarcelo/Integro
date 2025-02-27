from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel admin
    path('', include('inventario.urls')),  # Incluye las rutas de inventario desde la raíz
]