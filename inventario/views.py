from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dispositivo, DispositivoEstado, DispositivoUbicacion
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dispositivo, DispositivoEstado, DispositivoUbicacion, DispositivoCaracteristica

@login_required
def cliente_dispositivos(request):
    # Filtrar dispositivos del usuario logueado
    dispositivos = Dispositivo.objects.filter(propietario=request.user)
    
    # Preparar datos para la vista
    dispositivos_data = []
    for dispositivo in dispositivos:
        ultimo_estado = DispositivoEstado.objects.filter(dispositivo_id_dispositivo=dispositivo).order_by('-fecha').first()
        ultima_ubicacion = DispositivoUbicacion.objects.filter(dispositivo_id_dispositivo=dispositivo).order_by('-fecha').first()
        data = {
            'nomenclatura': dispositivo.nomenclatura,
            'serie': dispositivo.serie or '-',
            'tipo': dispositivo.tipo_dispositivo.nombre,
            'marca': dispositivo.modelo.marca_id_marca.nombre if dispositivo.modelo else '-',
            'modelo': dispositivo.modelo.nombre if dispositivo.modelo else '-',
            'ubicacion': f"{ultima_ubicacion.ubicacion_id_ubicacion.agencia} - {ultima_ubicacion.ubicacion_id_ubicacion.piso}" if ultima_ubicacion else '-',
            'estado': ultimo_estado.estado_id_estado.nombre if ultimo_estado else '-',
            'caracteristicas_url': f"/cliente/dispositivos/{dispositivo.id}/caracteristicas/",
        }
        dispositivos_data.append(data)
    
    context = {
        'email': request.user.email,
        'gerencia': request.user.gerencia.nombre if request.user.gerencia else '-',
        'dispositivos': dispositivos_data,
    }
    return render(request, 'inventario/cliente_dispositivos.html', context)

@login_required
def cliente_caracteristicas(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id, propietario=request.user)
    caracteristicas = DispositivoCaracteristica.objects.filter(dispositivo_id_dispositivo=dispositivo)
    context = {
        'dispositivo': dispositivo,
        'caracteristicas': caracteristicas,
    }
    return render(request, 'inventario/cliente_caracteristicas.html', context)