from django.urls import path
from . import views

app_name = 'inventario' # ¡Asegúrate de tener esta línea!

urlpatterns = [
    path('', views.dashboard_view, name='home'),  

    # URLs para Dispositivo (Vistas basadas en clase - CBV)
    path('dispositivos/', views.DispositivoListView.as_view(), name='dispositivo_list'),
    path('dispositivos/nuevo/', views.DispositivoCreateView.as_view(), name='dispositivo_new'),
    path('dispositivos/editar/<int:pk>/', views.DispositivoUpdateView.as_view(), name='dispositivo_edit'),
    path('dispositivos/borrar/<int:pk>/', views.DispositivoDeleteView.as_view(), name='dispositivo_delete'),

    # URLs para TipoDispositivo (Vistas basadas en clase - CBV)
    path('tipos-dispositivo/', views.TipoDispositivoListView.as_view(), name='tipodispositivo_list'),
    path('tipos-dispositivo/nuevo/', views.TipoDispositivoCreateView.as_view(), name='tipodispositivo_new'),
    path('tipos-dispositivo/editar/<int:pk>/', views.TipoDispositivoUpdateView.as_view(), name='tipodispositivo_edit'),
    path('tipos-dispositivo/borrar/<int:pk>/', views.TipoDispositivoDeleteView.as_view(), name='tipodispositivo_delete'),



]