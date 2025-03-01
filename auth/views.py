from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.groups.filter(name='Cliente').exists():
            return '/cliente/dispositivos/'  # URL directa
        elif self.request.user.groups.filter(name='Gerente').exists():
            return '/gerente/dispositivos/'  # Pendiente, URL directa
        elif self.request.user.groups.filter(name='Agente').exists():
            return '/agente/inventario/'  # Pendiente, URL directa
        else:  # Administrador o sin rol
            return '/admin/'  # URL directa

class LogoutRedirectView(RedirectView):
    url = '/login/'