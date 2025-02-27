from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dispositivo, DispositivoEstado, DispositivoUbicacion

@login_required
def cliente_dispositivos(request):
    dispositivos = Dispositivo.objects.filter(propietario=request.user)
    for dispositivo in dispositivos:
        dispositivo.ultimo_estado = DispositivoEstado.objects.filter(
            dispositivo_id_dispositivo=dispositivo
        ).order_by('-fecha').first()
        dispositivo.ultima_ubicacion = DispositivoUbicacion.objects.filter(
            dispositivo_id_dispositivo=dispositivo
        ).order_by('-fecha').first()
    context = {
        'dispositivos': dispositivos,
        'email': request.user.email,
        'gerencia': request.user.gerencia.nombre if request.user.gerencia else '-',
    }
    return render(request, 'inventario/cliente_dispositivos.html', context)