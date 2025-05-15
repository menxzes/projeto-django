# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class RegistroForm(UserCreationForm):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        help_text="Digite apenas números (11 dígitos)",
        widget=forms.TextInput(attrs={'pattern': r'\d{11}', 'title': '11 dígitos numéricos'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'password1', 'password2']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError("CPF deve conter exatamente 11 dígitos numéricos")
        
        if CustomUser.objects.filter(cpf=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado")
            
        return cpf

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()