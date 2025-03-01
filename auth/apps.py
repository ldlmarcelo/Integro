from django.apps import AppConfig

class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'  # Mantiene el nombre de la carpeta
    label = 'custom_auth'  # Nuevo label único