from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin en /admin/
    path('', include('inventario.urls', namespace='inventario')),  # Rutas de la app desde la raíz
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Logout
]