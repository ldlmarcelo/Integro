from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventario.views import CustomLoginView, AdminRedirectView

urlpatterns = [
    path('admin/', AdminRedirectView.as_view(), name='admin'),  # Redirige "Cliente" al login
    path('', include('inventario.urls', namespace='inventario')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
]