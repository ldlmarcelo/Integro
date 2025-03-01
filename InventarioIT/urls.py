from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from auth.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin directo, sin RedirectView
    path('', include('auth.urls', namespace='custom_auth')),
    path('', include('inventario.urls', namespace='inventario')),
]