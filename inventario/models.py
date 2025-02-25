from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Modelos de Catálogo con "Eliminación Lógica" (campo is_active)

class Gerencia(models.Model):
    id_gerencia = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


class TipoDispositivo(models.Model):
    id_tipo_dispositivo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, verbose_name="Nombre")
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


class EstadoDispositivo(models.Model):
    id_estado_dispositivo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, verbose_name='Nombre')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    agencia = models.CharField(max_length=45, unique=False, verbose_name="Agencia")  # unique=False revisado
    piso = models.CharField(max_length=45, blank=True, null=True, verbose_name="Piso")  # Opcional
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    class Meta:
        unique_together = ('agencia', 'piso')  # Mantenemos unique_together

    def __str__(self):
        return f"{self.agencia} - Piso {self.piso}"


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, verbose_name="Nombre")
    marca_id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca_id_marca', verbose_name="Marca")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    class Meta:
        unique_together = ('nombre', 'marca_id_marca')

    def __str__(self):
        return f"{self.marca_id_marca.nombre} - {self.nombre}"  # Muestra "Marca - Modelo"


class Caracteristica(models.Model):
    id_caracteristica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, unique=True, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


class CantidadMemoria(models.Model):
    id_cantidad_memoria = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(unique=True, verbose_name="Cantidad (GB)")  # Cambiado a IntegerField
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return str(self.cantidad)  # Devuelve la cantidad como string para __str__


class TipoMemoria(models.Model):
    id_tipo_memoria = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica

    def __str__(self):
        return self.nombre


# Modelo para Características Específicas Unificado  <-  ¡¡¡MOVIDO  ARRIBA!!!
class CaracteristicaEspecifica(models.Model):
    id_caracteristica_especifica = models.AutoField(primary_key=True)
    caracteristica = models.ForeignKey(Caracteristica, models.DO_NOTHING, verbose_name="Característica")  # Caracteristica general
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, models.DO_NOTHING, verbose_name="Tipo de Dispositivo")  # Tipo de dispositivo al que aplica
    tipo_memoria = models.ForeignKey(TipoMemoria, models.DO_NOTHING, blank=True, null=True, verbose_name="Tipo de Memoria")
    cantidad_memoria = models.ForeignKey(CantidadMemoria, models.DO_NOTHING, blank=True, null=True, verbose_name="Cantidad de Memoria")
    tipo_procesador = models.CharField(max_length=45, blank=True, null=True, verbose_name="Tipo de Procesador")
    velocidad_red = models.CharField(max_length=45, blank=True, null=True, verbose_name="Velocidad de Red")  # Mantenido como CharField (revisar si cambiar a numerico)
    interfaz_conexion = models.CharField(max_length=45, blank=True, null=True, verbose_name="Interfaz de Conexión")
    is_active = models.BooleanField(default=True, verbose_name="Activo")  # Campo para eliminación lógica
    # ... otros campos específicos que quieras añadir para diferentes tipos de dispositivos ...

    def __str__(self):
        return f"{self.caracteristica.nombre} ({self.tipo_dispositivo.nombre})"


# Modelo de Usuario Personalizado (heredando de AbstractUser)
class CustomUser(AbstractUser):
    gerencia = models.ForeignKey(
        Gerencia,
        models.SET_NULL,  # Aplicamos SET_NULL aquí
        blank=True,
        null=True,
        verbose_name="Gerencia"
    )

    groups = models.ManyToManyField(
        'auth.Group',  # Usamos 'auth.Group' para referirnos al modelo Group original
        related_name='customuser_set',  # Nombre único para la relación inversa
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',  # Usamos 'auth.Permission' para el modelo Permission original
        related_name='customuser_set',  # Mismo nombre único para consistencia
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username  # O self.email, o lo que uses para identificar al usuario


# Modelo principal para Dispositivos (VERSIÓN MINIMALISTA)
class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    nomenclatura = models.CharField(unique=True, max_length=45, verbose_name="Nomenclatura")  # Requerido
    serie = models.CharField(max_length=45, blank=True, null=True, verbose_name="Número de Serie")  # Opcional
    jira = models.CharField(max_length=45, blank=True, null=True, verbose_name="Jira Ticket")  # Opcional
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, models.DO_NOTHING, verbose_name="Tipo de Dispositivo")  # Requerido
    propietario = models.ForeignKey(CustomUser, models.DO_NOTHING, verbose_name="Propietario")  # Requerido - Ahora apunta a CustomUser

    def __str__(self):
        return self.nomenclatura


# Tabla intermedia para la relación muchos a muchos entre Dispositivo y Caracteristica
class DispositivoCaracteristica(models.Model):
    id_dispositivo_caracteristica = models.AutoField(primary_key=True)
    dispositivo_id_dispositivo = models.ForeignKey(Dispositivo, models.DO_NOTHING, db_column='dispositivo_id_dispositivo', verbose_name="Dispositivo")
    caracteristica_especifica = models.ForeignKey(CaracteristicaEspecifica, models.DO_NOTHING, verbose_name="Característica Específica")  # REEMPLAZADO: ForeignKey a CaracteristicaEspecifica
    valor = models.CharField(max_length=45, verbose_name="Valor")  # Requerido

    class Meta:
        db_table = 'dispositivo_caracteristica'
        verbose_name = "Dispositivo Característica"
        verbose_name_plural = "Dispositivos Características"

    def __str__(self):
        return f"{self.dispositivo_id_dispositivo.nomenclatura} - {self.valor}"


# Modelos para el Historial (sin cambios en on_delete según discusión previa)

class DispositivoEstado(models.Model):
    id_dispositivo_estado = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha")  # Requerido
    comentario = models.CharField(max_length=45, blank=True, null=True, verbose_name="Comentario")  # Opcional
    dispositivo_id_dispositivo = models.ForeignKey(Dispositivo, models.CASCADE, db_column='dispositivo_id_dispositivo', verbose_name="Dispositivo")  # Requerido
    estado_id_estado = models.ForeignKey('EstadoDispositivo', models.DO_NOTHING, db_column='estado_id_estado', verbose_name="Estado")  # Requerido
    agente = models.ForeignKey( # Campo Agregado: Agente del cambio de Estado
        CustomUser,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Agente del Cambio de Estado",
        related_name='cambios_estado_dispositivo' # Opcional: nombre relación inversa
    )

    class Meta:
        verbose_name = "Dispositivo Estado"
        verbose_name_plural = "Dispositivos Estados"

    def __str__(self):
        return f"{self.dispositivo_id_dispositivo.nomenclatura} - {self.fecha} - {self.estado_id_estado.nombre}"


class DispositivoUbicacion(models.Model):
    id_dispositivo_ubicacion = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha")  # Requerido
    comentario = models.CharField(max_length=45, blank=True, null=True, verbose_name="Comentario")  # Opcional
    dispositivo_id_dispositivo = models.ForeignKey(Dispositivo, models.CASCADE, db_column='dispositivo_id_dispositivo', verbose_name="Dispositivo")  # Requerido
    ubicacion_id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_id_ubicacion', verbose_name="Ubicación")  # Requerido
    agente = models.ForeignKey( # Campo Agregado: Agente del cambio de Ubicación
        CustomUser,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Agente del Cambio de Ubicación",
        related_name='cambios_ubicacion_dispositivo' # Opcional: nombre relación inversa
    )

    class Meta:
        verbose_name = "Dispositivo Ubicación"
        verbose_name_plural = "Dispositivos Ubicaciones"

    def __str__(self):
        return f"{self.dispositivo_id_dispositivo.nomenclatura} - {self.fecha} - {self.ubicacion_id_ubicacion.agencia}, {self.ubicacion_id_ubicacion.piso}"


class DispositivoPropietarioHistorico(models.Model):
    id_dispositivo_propietario_historico = models.AutoField(primary_key=True)
    dispositivo = models.ForeignKey(Dispositivo, models.CASCADE, verbose_name="Dispositivo")  # Requerido
    propietario_id_anterior = models.ForeignKey(CustomUser, models.SET_NULL, db_column='propietario_id_anterior', blank=True, null=True, related_name='%(class)s_anterior', verbose_name="Propietario Anterior")  # Opcional - Aplicamos SET_NULL
    propietario_id_nuevo = models.ForeignKey(CustomUser, models.SET_NULL, db_column='propietario_id_nuevo', related_name='%(class)s_nuevo', verbose_name="Propietario Nuevo", blank=True, null=True)  # Requerido - Aplicamos SET_NULL
    fecha_cambio = models.DateTimeField(verbose_name="Fecha de Cambio")  # Requerido
    comentario = models.CharField(max_length=255, blank=True, null=True, verbose_name="Comentario")  # Opcional
    agente = models.ForeignKey( # Campo Agregado: Agente del cambio de Propietario
        CustomUser,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Agente del Cambio de Propietario",
        related_name='cambios_propietario_historico' # Opcional: nombre relación inversa
    )

    class Meta:
        verbose_name = "Dispositivo Propietario Histórico"
        verbose_name_plural = "Dispositivos Propietarios Históricos"

    def __str__(self):
        return f"{self.dispositivo.nomenclatura} - {self.fecha_cambio} - De: {self.propietario_id_anterior} a: {self.propietario_id_nuevo}"