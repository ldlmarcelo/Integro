from django.contrib import admin
from .models import (
    Area,
    CustomUser,
    Dispositivo,
    EstadoDispositivo,
    Gerencia,
    TipoDispositivo,
    # CantidadMemoria,  <- ¡IMPORTACIÓN ELIMINADA!
)

# Define los modelos que se mostrarán en el admin y personaliza su visualización

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(EstadoDispositivo)
class EstadoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Gerencia)
class GerenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'serial', 'fecha_alta', 'tipo_dispositivo', 'estado_dispositivo', 'area', 'usuario')
    list_filter = ('tipo_dispositivo', 'estado_dispositivo', 'area', 'usuario')
    search_fields = ('nombre', 'marca', 'modelo', 'serial')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'gerencia', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gerencia')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Gerencia y Permisos', {'fields': ('gerencia', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Estado', {'fields': ('is_active',)})
    )
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')


#  ¡COMENTARIO ELIMINADO! Ya no es necesario registrar CantidadMemoriaAdmin porque no existe el modelo
# @admin.register(CantidadMemoria)
# class CantidadMemoriaAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'valor') # Ajusta los campos a mostrar
#     search_fields = ('nombre',) # Ajusta los campos de búsqueda