from django.contrib import admin
from .models import (
    Gerencia, CustomUser, TipoDispositivo, CantidadMemoria,
    Marca, TipoMemoria, Modelo, Estado, Ubicacion,
    Caracteristica, CaracteristicaEspecifica, Dispositivo,
    DispositivoCaracteristica, DispositivoEstado,
    DispositivoUbicacion, DispositivoPropietarioHistorico
)

# Register your models here.

@admin.register(Gerencia)
class GerenciaAdmin(admin.ModelAdmin):
    # list_display = ('nombre',)  # COMENTAR ESTA LÍNEA
    # list_filter = ('nombre',)   # COMENTAR ESTA LÍNEA
    # search_fields = ('nombre',)  # COMENTAR ESTA LÍNEA
    pass # DEJAR SOLO EL 'pass'

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'gerencia', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gerencia') # Filtro por gerencia y estado de usuario
    search_fields = ('username', 'first_name', 'last_name', 'email') # Buscar por campos de usuario
admin.site.register(CustomUser, CustomUserAdmin) # <<--- ¡CORREGIDO AQUÍ!

class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Campos a mostrar en la lista
    list_filter = ('nombre',)   # Campos para filtrar en la barra lateral
    search_fields = ('nombre',)  # Campos para buscar en la barra de búsqueda
admin.site.register(TipoDispositivo, TipoDispositivoAdmin)

class CantidadMemoriaAdmin(admin.ModelAdmin):
    list_display = ('cantidad',)
    list_filter = ('cantidad',) # Añadido filtro por cantidad
    search_fields = ('cantidad',)
admin.site.register(CantidadMemoria, CantidadMemoriaAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Marca, MarcaAdmin)

class TipoMemoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',) # Añadido filtro por nombre
    search_fields = ('nombre',)
admin.site.register(TipoMemoria, TipoMemoriaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca_id_marca') # Mostrar marca en la lista
    list_filter = ('marca_id_marca',) # Filtrar por marca
    search_fields = ('nombre', 'marca_id_marca__nombre') # Buscar por nombre de modelo y nombre de marca (relacionado)
admin.site.register(Modelo, ModeloAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',) # Añadido filtro por nombre
    search_fields = ('nombre',)
admin.site.register(Estado, EstadoAdmin)

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('agencia', 'piso')
    list_filter = ('agencia',) # Filtrar por agencia
    search_fields = ('agencia', 'piso') # Buscar por agencia y piso
admin.site.register(Ubicacion, UbicacionAdmin)

class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',) # Añadido filtro por nombre
    search_fields = ('nombre',)
admin.site.register(Caracteristica, CaracteristicaAdmin)

class CaracteristicaEspecificaAdmin(admin.ModelAdmin):
    list_display = ('caracteristica', 'tipo_dispositivo', 'tipo_memoria', 'cantidad_memoria') # Mostrar campos clave
    list_filter = ('caracteristica', 'tipo_dispositivo', 'tipo_memoria', 'cantidad_memoria') # Filtrar por campos clave
    search_fields = (
        'caracteristica__nombre', 'tipo_dispositivo__nombre',
        'tipo_memoria__nombre', 'cantidad_memoria__cantidad',
        'tipo_procesador', 'velocidad_red', 'interfaz_conexion' # Añadido campos de búsqueda
    )
admin.site.register(CaracteristicaEspecifica, CaracteristicaEspecificaAdmin)

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nomenclatura', 'tipo_dispositivo', 'propietario') # Campos principales a mostrar
    list_filter = ('tipo_dispositivo', 'propietario') # Filtrar por tipo y propietario
    search_fields = ('nomenclatura', 'serie', 'jira', 'propietario__username', 'propietario__first_name', 'propietario__last_name') # Búsqueda más amplia
admin.site.register(Dispositivo, DispositivoAdmin)

class DispositivoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'caracteristica_especifica', 'valor')
    list_filter = ('dispositivo_id_dispositivo', 'caracteristica_especifica__caracteristica', 'caracteristica_especifica__tipo_dispositivo') # Filtrar por dispositivo y caracteristica especifica
    search_fields = (
        'dispositivo_id_dispositivo__nomenclatura', 'caracteristica_especifica__caracteristica__nombre',
        'caracteristica_especifica__tipo_dispositivo__nombre', 'valor' # Campos de búsqueda
    )
    
admin.site.register(DispositivoCaracteristica, DispositivoCaracteristicaAdmin)

class DispositivoEstadoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'estado_id_estado')
    list_filter = ('estado_id_estado', 'dispositivo_id_dispositivo', 'fecha') # Filtrar por estado, dispositivo y fecha
    search_fields = (
        'dispositivo_id_dispositivo__nomenclatura', 'estado_id_estado__nombre', 'comentario' # Campos de búsqueda
    )
    date_hierarchy = 'fecha' # Permite la navegación por fechas
admin.site.register(DispositivoEstado, DispositivoEstadoAdmin)

class DispositivoUbicacionAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'ubicacion_id_ubicacion')
    list_filter = ('ubicacion_id_ubicacion', 'dispositivo_id_dispositivo', 'fecha') # Filtrar por ubicacion, dispositivo y fecha
    search_fields = (
        'dispositivo_id_dispositivo__nomenclatura', 'ubicacion_id_ubicacion__agencia',
        'ubicacion_id_ubicacion__piso', 'comentario' # Campos de búsqueda
    )
    date_hierarchy = 'fecha' # Navegación por fechas
admin.site.register(DispositivoUbicacion, DispositivoUbicacionAdmin)

class DispositivoPropietarioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'fecha_cambio', 'propietario_id_nuevo')
    list_filter = ('dispositivo', 'propietario_id_nuevo', 'propietario_id_anterior', 'fecha_cambio') # Filtrar por dispositivo, propietarios y fecha
    search_fields = (
        'dispositivo__nomenclatura', 'propietario_id_nuevo__username',
        'propietario_id_anterior__username', 'comentario' # Campos de búsqueda
    )
    date_hierarchy = 'fecha_cambio' # Navegación por fechas
admin.site.register(DispositivoPropietarioHistorico, DispositivoPropietarioHistoricoAdmin)