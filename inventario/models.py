from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Asegúrate de que esta clase Gerencia esté definida en tu archivo models.py
# Si no lo está, deberás definirla también (la definición de Gerencia no ha sido provista en este chat previo).
# Asumo que Gerencia está en la misma app 'inventario' o 'app_inventario', ajusta si es diferente.
class Gerencia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Gerencia")

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    gerencia = models.ForeignKey(
        'inventario.Gerencia', # o 'app_inventario.Gerencia', ajusta según tu app
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Gerencia",
        related_name="custom_users" # Related name añadido para claridad
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Dispositivo(models.Model): # Asegúrate del modelo base correcto si no es models.Model
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100, unique=True)
    fecha_alta = models.DateField(verbose_name='Fecha de Alta')
    fecha_baja = models.DateField(verbose_name='Fecha de Baja', null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    tipo_dispositivo = models.ForeignKey('TipoDispositivo', models.DO_NOTHING, verbose_name='Tipo de Dispositivo')
    estado_dispositivo = models.ForeignKey('EstadoDispositivo', models.DO_NOTHING, verbose_name='Estado del Dispositivo')
    area = models.ForeignKey('Area', models.DO_NOTHING, verbose_name='Área')

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Usuario Asignado",
        related_name="dispositivos_asignados" # Related name añadido para claridad
    )

    def __str__(self):
        return self.nombre


class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Tipo de Dispositivo')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

class EstadoDispositivo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Estado del Dispositivo')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Área')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre