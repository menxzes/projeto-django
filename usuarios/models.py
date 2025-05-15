from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    # Herda todos os campos padrão do User (username, email, password, etc.)
    TIPO_CHOICES = [
        ('C', 'Cliente'),
        ('A', 'Administrador'),
    ]
    
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CHOICES,
        default='C',
        verbose_name='Tipo de Usuário'
    )
    
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Formato: '+999999999'. Até 15 dígitos."
        )],
        blank=True,
        null=True
    )
    
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(
            regex=r'^\d{11}$',
            message="CPF deve conter 11 dígitos."
        )],
        blank=True,
        null=True,
        verbose_name='CPF'
    )
    
    class Meta:
        verbose_name = "Usuário do Sistema"
        verbose_name_plural = "Usuários do Sistema"
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_tipo_display()})"

    @property
    def is_cliente(self):
        return self.tipo == 'C'
    
    @property
    def is_admin(self):
        return self.tipo == 'A'