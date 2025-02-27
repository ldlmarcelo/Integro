from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Gerencia,
    CustomUser,
    Dispositivo,
    TipoDispositivo,
    EstadoDispositivo,
    Ubicacion,
    Marca,
    Modelo,
    Caracteristica,
    CantidadMemoria,
    TipoMemoria,
    DispositivoCaracteristica,
    DispositivoEstado,
    DispositivoUbicacion,
    DispositivoPropietarioHistorico,
)

@admin.register(Gerencia)
class GerenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'gerencia', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gerencia')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Gerencia y Permisos', {'fields': ('gerencia', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Estado', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'gerencia', 'is_staff', 'is_active'),
        }),
    )

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(EstadoDispositivo)
class EstadoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('agencia', 'piso', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('agencia', 'piso')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca_id_marca', 'is_active')
    list_filter = ('is_active', 'marca_id_marca')
    search_fields = ('nombre', 'marca_id_marca__nombre')

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(CantidadMemoria)
class CantidadMemoriaAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('cantidad',)

@admin.register(TipoMemoria)
class TipoMemoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nomenclatura', 'serie', 'jira', 'tipo_dispositivo', 'propietario')
    list_filter = ('tipo_dispositivo', 'propietario')
    search_fields = ('nomenclatura', 'serie', 'jira')

@admin.register(DispositivoCaracteristica)
class DispositivoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'caracteristica_especifica', 'valor')
    list_filter = ('dispositivo_id_dispositivo', 'caracteristica_especifica')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'caracteristica_especifica__nombre', 'valor')

@admin.register(DispositivoEstado)
class DispositivoEstadoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'estado_id_estado', 'comentario', 'agente')
    list_filter = ('dispositivo_id_dispositivo', 'fecha', 'estado_id_estado', 'agente')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'estado_id_estado__nombre', 'comentario', 'agente__username')
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)

@admin.register(DispositivoUbicacion)
class DispositivoUbicacionAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'ubicacion_id_ubicacion', 'comentario', 'agente')
    list_filter = ('dispositivo_id_dispositivo', 'fecha', 'ubicacion_id_ubicacion', 'agente')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'ubicacion_id_ubicacion__agencia', 'ubicacion_id_ubicacion__piso', 'comentario', 'agente__username')
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)

@admin.register(DispositivoPropietarioHistorico)
class DispositivoPropietarioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'fecha_cambio', 'propietario_id_anterior', 'propietario_id_nuevo', 'agente', 'comentario')
    list_filter = ('dispositivo', 'fecha_cambio', 'propietario_id_anterior', 'propietario_id_nuevo', 'agente')
    search_fields = ('dispositivo__nomenclatura', 'propietario_id_anterior__username', 'propietario_id_nuevo__username', 'agente__username', 'comentario')
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)