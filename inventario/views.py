from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from .models import Dispositivo, DispositivoEstado, DispositivoUbicacion, DispositivoCaracteristica, TipoDispositivo, Modelo

# Vista para el Cliente con validación de rol
class ClienteDispositivosView(UserPassesTestMixin, TemplateView):
    template_name = 'inventario/cliente_dispositivos.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Cliente').exists()

    def handle_no_permission(self):
        return render(self.request, 'inventario/error_rol.html', {'message': 'No tenés permisos para ver esta página.'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dispositivos = Dispositivo.objects.filter(propietario=self.request.user)
        dispositivos_data = []
        for dispositivo in dispositivos:
            tipo = dispositivo.tipo_dispositivo
            marca = tipo.modelo.marca_id_marca.nombre if hasattr(tipo, 'modelo') and tipo.modelo else '-'
            modelo = tipo.modelo.nombre if hasattr(tipo, 'modelo') and tipo.modelo else '-'
            ultimo_estado = DispositivoEstado.objects.filter(dispositivo_id_dispositivo=dispositivo).order_by('-fecha').first()
            ultima_ubicacion = DispositivoUbicacion.objects.filter(dispositivo_id_dispositivo=dispositivo).order_by('-fecha').first()
            data = {
                'nomenclatura': dispositivo.nomenclatura,
                'serie': dispositivo.serie or '-',
                'tipo': tipo.nombre,
                'marca': marca,
                'modelo': modelo,
                'ubicacion': f"{ultima_ubicacion.ubicacion_id_ubicacion.agencia} - {ultima_ubicacion.ubicacion_id_ubicacion.piso}" if ultima_ubicacion else '-',
                'estado': ultimo_estado.estado_id_estado.nombre if ultimo_estado else '-',
                'caracteristicas_url': f"/cliente/dispositivos/{dispositivo.id}/caracteristicas/",
            }
            dispositivos_data.append(data)
        
        context.update({
            'email': self.request.user.email,
            'gerencia': self.request.user.gerencia.nombre if self.request.user.gerencia else '-',
            'dispositivos': dispositivos_data,
        })
        return context

class ClienteCaracteristicasView(UserPassesTestMixin, TemplateView):
    template_name = 'inventario/cliente_caracteristicas.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Cliente').exists()

    def handle_no_permission(self):
        return render(self.request, 'inventario/error_rol.html', {'message': 'No tenés permisos para ver esta página.'})

    def get_context_data(self, **kwargs):
        dispositivo_id = kwargs.get('dispositivo_id')
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id, propietario=self.request.user)
        caracteristicas = DispositivoCaracteristica.objects.filter(dispositivo_id_dispositivo=dispositivo)
        return {
            'dispositivo': dispositivo,
            'caracteristicas': caracteristicas,
        }