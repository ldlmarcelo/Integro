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
    def has_module_permission(self, request):
        # Solo Admin ve Gerencia
        return request.user.groups.filter(name='Administrador').exists()

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
    def has_module_permission(self, request):
        # Solo Admin ve CustomUser
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    def has_module_permission(self, request):
        # Solo Admin ve TipoDispositivo
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(EstadoDispositivo)
class EstadoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    def has_module_permission(self, request):
        # Solo Admin ve EstadoDispositivo
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('agencia', 'piso', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('agencia', 'piso')
    def has_module_permission(self, request):
        # Solo Admin ve Ubicacion
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    def has_module_permission(self, request):
        # Solo Admin ve Marca
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca_id_marca', 'is_active')
    list_filter = ('is_active', 'marca_id_marca')
    search_fields = ('nombre', 'marca_id_marca__nombre')
    def has_module_permission(self, request):
        # Solo Admin ve Modelo
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    def has_module_permission(self, request):
        # Solo Admin ve Caracteristica
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(CantidadMemoria)
class CantidadMemoriaAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('cantidad',)
    def has_module_permission(self, request):
        # Solo Admin ve CantidadMemoria
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(TipoMemoria)
class TipoMemoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    def has_module_permission(self, request):
        # Solo Admin ve TipoMemoria
        return request.user.groups.filter(name='Administrador').exists()

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nomenclatura', 'serie', 'jira', 'tipo_dispositivo', 'propietario')
    list_filter = ('tipo_dispositivo', 'propietario')
    search_fields = ('nomenclatura', 'serie', 'jira')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Gerente').exists():
            return qs.filter(propietario__gerencia=request.user.gerencia) | qs.filter(propietario=request.user)
        elif request.user.groups.filter(name='Cliente').exists():
            return qs.filter(propietario=request.user)
        return qs
    def has_add_permission(self, request):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()

@admin.register(DispositivoCaracteristica)
class DispositivoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'caracteristica_especifica', 'valor')
    list_filter = ('dispositivo_id_dispositivo', 'caracteristica_especifica')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'caracteristica_especifica__nombre', 'valor')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Gerente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario__gerencia=request.user.gerencia) | qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        elif request.user.groups.filter(name='Cliente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        return qs
    def has_add_permission(self, request):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()

@admin.register(DispositivoEstado)
class DispositivoEstadoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'estado_id_estado', 'comentario', 'agente')
    list_filter = ('dispositivo_id_dispositivo', 'fecha', 'estado_id_estado', 'agente')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'estado_id_estado__nombre', 'comentario', 'agente__username')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Gerente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario__gerencia=request.user.gerencia) | qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        elif request.user.groups.filter(name='Cliente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        return qs
    def has_add_permission(self, request):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)

@admin.register(DispositivoUbicacion)
class DispositivoUbicacionAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id_dispositivo', 'fecha', 'ubicacion_id_ubicacion', 'comentario', 'agente')
    list_filter = ('dispositivo_id_dispositivo', 'fecha', 'ubicacion_id_ubicacion', 'agente')
    search_fields = ('dispositivo_id_dispositivo__nomenclatura', 'ubicacion_id_ubicacion__agencia', 'ubicacion_id_ubicacion__piso', 'comentario', 'agente__username')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Gerente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario__gerencia=request.user.gerencia) | qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        elif request.user.groups.filter(name='Cliente').exists():
            return qs.filter(dispositivo_id_dispositivo__propietario=request.user)
        return qs
    def has_add_permission(self, request):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)

@admin.register(DispositivoPropietarioHistorico)
class DispositivoPropietarioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'fecha_cambio', 'propietario_id_anterior', 'propietario_id_nuevo', 'agente', 'comentario')
    list_filter = ('dispositivo', 'fecha_cambio', 'propietario_id_anterior', 'propietario_id_nuevo', 'agente')
    search_fields = ('dispositivo__nomenclatura', 'propietario_id_anterior__username', 'propietario_id_nuevo__username', 'agente__username', 'comentario')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Gerente').exists():
            return qs.filter(dispositivo__propietario__gerencia=request.user.gerencia) | qs.filter(dispositivo__propietario=request.user)
        elif request.user.groups.filter(name='Cliente').exists():
            return qs.filter(dispositivo__propietario=request.user)
        return qs
    def has_add_permission(self, request):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name__in=['Gerente', 'Cliente']).exists()
    def save_model(self, request, obj, form, change):
        if not obj.agente:
            obj.agente = request.user
        super().save_model(request, obj, form, change)