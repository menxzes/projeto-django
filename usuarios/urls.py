from django.urls import path
from . import views
from .views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]