from django import forms
from inventario.models import (
    Dispositivo,
    TipoDispositivo,
    Marca,
    Modelo,
    CustomUser,
    Ubicacion,
    Estado,
    Caracteristica,
    CaracteristicaEspecifica,
    CantidadMemoria,
    TipoMemoria,
    Gerencia
)

# Formulario para el modelo Dispositivo
class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo # Asocia este formulario con el modelo Dispositivo
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo TipoDispositivo
class TipoDispositivoForm(forms.ModelForm):
    class Meta:
        model = TipoDispositivo # Asocia este formulario con el modelo TipoDispositivo
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo Marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca # Asocia este formulario con el modelo Marca
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo Modelo
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo # Asocia este formulario con el modelo Modelo
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo CustomUser
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser # Asocia este formulario con el modelo CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'gerencia', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'] #  Seleccionamos campos relevantes para el formulario inicial de Usuario

# Formulario para el modelo Ubicacion
class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion # Asocia este formulario con el modelo Ubicacion
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo Estado
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado # Asocia este formulario con el modelo Estado
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo Caracteristica
class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica # Asocia este formulario con el modelo Caracteristica
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo CaracteristicaEspecifica
class CaracteristicaEspecificaForm(forms.ModelForm):
    class Meta:
        model = CaracteristicaEspecifica # Asocia este formulario con el modelo CaracteristicaEspecifica
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo CantidadMemoria
class CantidadMemoriaForm(forms.ModelForm):
    class Meta:
        model = CantidadMemoria # Asocia este formulario con el modelo CantidadMemoria
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo TipoMemoria
class TipoMemoriaForm(forms.ModelForm):
    class Meta:
        model = TipoMemoria # Asocia este formulario con el modelo TipoMemoria
        fields = '__all__' # Incluye todos los campos del modelo en el formulario

# Formulario para el modelo Gerencia
class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia # Asocia este formulario con el modelo Gerencia
        fields = '__all__' # Incluye todos los campos del modelo en el formulario