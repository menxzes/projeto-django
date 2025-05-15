from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# from django.contrib.auth.models import Group

admin.site.site_header = "Agenda Fácil - Administração"
admin.site.index_title = "Painel de Controle"

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo', 'is_staff')
    list_filter = ('tipo', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'telefone', 'cpf')}),
        ('Permissões', {'fields': ('tipo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    def get_app_label(self, request):
        return "Controle de Acesso"

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.unregister(Group)