from django.contrib import admin
from django.urls import path, include
from inventario import views # ¡Importante: importar las vistas de la APP inventario!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls', namespace='inventario')), # ¡Línea para incluir las URLs de la APP!
    path('', views.dashboard_view, name='home'), # ¡Línea para la URL raíz (Dashboard)!
]