"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import redirecionar_por_tipo
from usuarios.views import registro

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota principal: redireciona usuários após login com base no tipo
    path('inicio/', redirecionar_por_tipo, name='redirecionar_por_tipo'),

    # App de agendamentos
    path('', include('agendamentos.urls')),

    # Autenticação: login, logout, password_reset etc.
    path('', include('django.contrib.auth.urls')),

    # Registro de usuários (rota direta, sem necessidade de include extra)
    path('registro/', registro, name='registro'),
]
