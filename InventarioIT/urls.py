from django.contrib import admin
from django.urls import path, include
from inventario import views  # ¡Importante: importar las vistas de la APP inventario para el dashboard!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),  # ¡Incluye las URLs de la APP inventario BAJO el prefijo /inventario/ !
    path('', views.dashboard_view, name='home'),  # URL para la raíz (Dashboard) - ¡MANTENER ESTA LÍNEA!
]