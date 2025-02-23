from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import DispositivoForm, TipoDispositivoForm
from .models import Dispositivo, TipoDispositivo, Ubicacion, Estado

# --- Vistas para Dispositivo ---
class DispositivoListView(ListView):
    model = Dispositivo
    template_name = 'inventario/dispositivo/dispositivo_list.html' # Ruta al template CORRECTA (subdirectorio 'dispositivo')
    context_object_name = 'dispositivos'

class DispositivoCreateView(CreateView):
    model = Dispositivo
    form_class = DispositivoForm
    template_name = 'inventario/dispositivo/dispositivo_form.html' # Ruta al template CORRECTA (subdirectorio 'dispositivo')
    success_url = reverse_lazy('inventario:dispositivo_list')

class DispositivoUpdateView(UpdateView):
    model = Dispositivo
    form_class = DispositivoForm
    template_name = 'inventario/dispositivo/dispositivo_form.html' # Ruta al template CORRECTA (subdirectorio 'dispositivo')
    success_url = reverse_lazy('inventario:dispositivo_list')

class DispositivoDeleteView(DeleteView):
    model = Dispositivo
    template_name = 'inventario/dispositivo/dispositivo_confirm_delete.html' # Ruta al template CORRECTA (subdirectorio 'dispositivo')
    success_url = reverse_lazy('inventario:dispositivo_list')
    context_object_name = 'dispositivo'

# --- Vistas para TipoDispositivo ---
class TipoDispositivoListView(ListView):
    model = TipoDispositivo
    template_name = 'inventario/tipodispositivo/tipodispositivo_list.html' # Ruta al template CORRECTA (subdirectorio 'tipodispositivo')
    context_object_name = 'tipos_dispositivo'

class TipoDispositivoCreateView(CreateView):
    model = TipoDispositivo
    form_class = TipoDispositivoForm
    template_name = 'inventario/tipodispositivo/tipodispositivo_form.html' # Ruta al template CORRECTA (subdirectorio 'tipodispositivo')
    success_url = reverse_lazy('inventario:tipodispositivo_list')

class TipoDispositivoUpdateView(UpdateView):
    model = TipoDispositivo
    form_class = TipoDispositivoForm
    template_name = 'inventario/tipodispositivo/tipodispositivo_form.html' # Ruta al template CORRECTA (subdirectorio 'tipodispositivo')
    success_url = reverse_lazy('inventario:tipodispositivo_list')

class TipoDispositivoDeleteView(DeleteView):
    model = TipoDispositivo
    template_name = 'inventario/tipodispositivo/tipodispositivo_confirm_delete.html' # Ruta al template CORRECTA (subdirectorio 'tipodispositivo')
    success_url = reverse_lazy('inventario:tipodispositivo_list')
    context_object_name = 'tipo_dispositivo'

# --- Vista para Dashboard ---
def dashboard_view(request):
    user = request.user
    is_gerente = user.groups.filter(name='Gerentes').exists()
    is_agente = user.groups.filter(name='Agentes').exists()

    context = {
        'user': user,
        'is_gerente': is_gerente,
        'is_agente': is_agente,
    }
    return render(request, 'inventario/dashboard.html', context)

from django.shortcuts import render, HttpResponse  # Asegúrate de tener HttpResponse importado

def dispositivo_list(request):
    return HttpResponse("<h1>Lista de Dispositivos (Placeholder)</h1>")

def tipodispositivo_list(request):
    return HttpResponse("<h1>Lista de Tipos de Dispositivo (Placeholder)</h1>")

def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'inventario/ubicacion/ubicacion_list.html', {'ubicaciones': ubicaciones})

def estado_list(request):
    estados = Estado.objects.all()  # Consulta a la base de datos para obtener TODOS los estados
    return render(request, 'inventario/estado/estado_list.html', {
        'estados': estados  # Pasa la lista de estados al template con la clave 'estados'
    })