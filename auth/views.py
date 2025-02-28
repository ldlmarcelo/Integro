from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.groups.filter(name='Cliente').exists():
            return reverse_lazy('inventario:cliente_dispositivos')
        elif self.request.user.groups.filter(name='Gerente').exists():
            return reverse_lazy('inventario:gerente_dispositivos')
        elif self.request.user.groups.filter(name='Agente').exists():
            return reverse_lazy('inventario:agente_inventario')
        else:  # Administrador o sin rol
            return '/admin/'

class LogoutRedirectView(RedirectView):
    url = '/login/'

class AdminRedirectView(UserPassesTestMixin, RedirectView):
    url = '/login/'

    def test_func(self):
        return not self.request.user.groups.filter(name__in=['Cliente', 'Gerente', 'Agente']).exists()