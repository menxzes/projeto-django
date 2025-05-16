from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
import re

class RegistroForm(UserCreationForm):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '00000000000'})
    )
    
    telefone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+5511999999999'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'telefone', 'password1', 'password2']
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not re.match(r'^\d{11}$', cpf):
            raise ValidationError("CPF deve conter exatamente 11 dígitos")
        
        if len(set(cpf)) == 1:
            raise ValidationError("CPF inválido")
            
        return cpf
    
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone and not re.match(r'^\+?1?\d{9,15}$', telefone):
            raise ValidationError("Formato: +5599999999999")
        return telefone
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipo = 'C'         # Garante que o usuário é cliente
        user.is_staff = False   # Garantia extra que cliente não terá acesso admin
        if commit:
            user.save()
        return user