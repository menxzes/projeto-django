from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import RegistroForm

class CustomUserAdmin(UserAdmin):
    add_form = RegistroForm
    list_display = ('username', 'email', 'cpf', 'tipo', 'is_active')
    list_filter = ('tipo',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'cpf', 'telefone')}),
        ('Permissões', {'fields': ('tipo', 'is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)