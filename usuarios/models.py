from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    
    TIPO_CHOICES = [
        ('C', 'Cliente'),
        ('A', 'Administrador'),
    ]
    
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False, 
        blank=False,
        default='00000000000',
        validators=[RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos')],
        help_text="Somente números",
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False, 
        default='+5500000000000',
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Formato: +5599999999999')],
    )
    
    
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='C')
    
    class Meta:
        verbose_name = "Usuário do Sistema"
        verbose_name_plural = "Usuários do Sistema"
    
    def __str__(self):
        return f"{self.get_full_name()} (CPF: {self.cpf})"

    @property
    def is_cliente(self):
        return self.tipo == 'C'
    
    @property
    def is_admin(self):
        return self.tipo == 'A'