from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    
    TIPO_CHOICES = [
        ('C', 'Cliente'),
        ('A', 'Administrador'),
    ]
    
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='C')
    
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False, 
        blank=False,
        default='00000000000'
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False, 
        default=''
    )
    
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