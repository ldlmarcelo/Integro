from django.urls import path
from . import views

app_name = 'custom_auth'  # Nuevo namespace

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutRedirectView.as_view(), name='logout'),
]