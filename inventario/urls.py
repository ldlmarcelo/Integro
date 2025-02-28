from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventario.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls', namespace='inventario')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
]