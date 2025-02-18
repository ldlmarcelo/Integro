from django.contrib import admin
from .models import (
    Gerencia, CustomUser, TipoDispositivo, CantidadMemoria,
    Marca, TipoMemoria, Modelo, Estado, Ubicacion,
    Caracteristica, CaracteristicaEspecifica, Dispositivo,
    DispositivoCaracteristica, DispositivoEstado,
    DispositivoUbicacion, DispositivoPropietarioHistorico
)

# Register your models here.
admin.site.register(Gerencia)
admin.site.register(CustomUser)
admin.site.register(TipoDispositivo)
admin.site.register(CantidadMemoria)
admin.site.register(Marca)
admin.site.register(TipoMemoria)
admin.site.register(Modelo)
admin.site.register(Estado)
admin.site.register(Ubicacion)
admin.site.register(Caracteristica)
admin.site.register(CaracteristicaEspecifica)
admin.site.register(Dispositivo)
admin.site.register(DispositivoCaracteristica)
admin.site.register(DispositivoEstado)
admin.site.register(DispositivoUbicacion)
admin.site.register(DispositivoPropietarioHistorico)