from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from usuarios.models import CustomUser

class Servico(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'Já existe um serviço com este nome.'
        }
    )
    descricao = models.TextField(
        blank=True,
        verbose_name='Descrição'
    )
    duracao = models.PositiveIntegerField(
        default=60,
        editable=False,
        verbose_name='Duração (minutos)'
    )
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço'
    )
    ativo = models.BooleanField(
        default=True,
        help_text='Serviços inativos não aparecem para agendamento.'
    )

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.duracao}min)"


class Profissional(models.Model):
    usuario = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'A'},  # Só admins podem ser profissionais
        related_name='profissional'
    )
    servico = models.ForeignKey(
        Servico,
        on_delete=models.PROTECT,
        verbose_name='Serviço'
    )
    horarios_disponiveis = models.JSONField(
        default=list,
        help_text='Lista de horários no formato ["08:00", "09:00", ...]'
    )

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'servico'],
                name='unique_profissional_servico'
            )
        ]

    def clean(self):
        # Valida se o usuário é realmente um administrador
        if not self.usuario.is_admin:
            raise ValidationError(
                {'usuario': 'O profissional deve ser um usuário administrador.'}
            )

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.servico.nome}"


class Agendamento(models.Model):
    cliente = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='agendamentos_cliente',
        limit_choices_to={'tipo': 'C'}  # Só clientes podem agendar
    )
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.PROTECT,
        related_name='agendamentos_profissional'
    )
    data = models.DateField(
        verbose_name='Data do Agendamento'
    )
    horario = models.CharField(
        max_length=5,
        verbose_name='Horário (HH:MM)'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    STATUS_CHOICES = [
        ('A', 'Agendado'),
        ('C', 'Cancelado'),
        ('F', 'Finalizado'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data', 'horario']
        constraints = [
            models.UniqueConstraint(
                fields=['profissional', 'data', 'horario'],
                name='unique_agendamento_profissional_horario',
                condition=models.Q(status='A')
            )
        ]

    def clean(self):
        super().clean()

        conflitos = Agendamento.objects.filter(
            profissional=self.profissional,
            data=self.data,
            horario=self.horario,
            status='A'
        ).exclude(pk=self.pk)

        if conflitos.exists():
            raise ValidationError(
                f"Horário já ocupado pelo cliente {conflitos.first().cliente.username}"
            )
        
        try:
            # Converte o horário string para objeto time
            hora_obj = datetime.strptime(self.horario, '%H:%M').time()
            
            # Combina com a data e adiciona o fuso horário
            data_hora_agendamento = timezone.make_aware(
                datetime.combine(self.data, hora_obj)
            )
            
            # Compara com o horário atual (ambos com fuso horário)
            if data_hora_agendamento < timezone.now():
                raise ValidationError("Não é possível agendar no passado")
                
        except ValueError as e:
            raise ValidationError("Formato de horário inválido. Use HH:MM")

    def cancelar(self):
        self.status = 'C'
        self.save()

    def __str__(self):
        return (
            f"{self.cliente.get_short_name()} com "
            f"{self.profissional.usuario.get_short_name()} - "
            f"{self.data.strftime('%d/%m/%Y')} {self.horario}"
        )

    @property
    def data_hora_completa(self):
        from datetime import datetime
        return datetime.combine(
            self.data,
            datetime.strptime(self.horario, '%H:%M').time()
        )
