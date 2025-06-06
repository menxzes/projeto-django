# Generated by Django 4.2 on 2025-05-16 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendamentos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='especialidade',
            field=models.CharField(default='Especialidade', help_text='Informe a especialidade do profissional', max_length=100),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profissional', to=settings.AUTH_USER_MODEL),
        ),
    ]
