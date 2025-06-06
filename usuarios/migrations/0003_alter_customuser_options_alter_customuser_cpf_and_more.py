# Generated by Django 4.2 on 2025-05-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_populate_cpf_telefone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Usuário do Sistema', 'verbose_name_plural': 'Usuários do Sistema'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefone',
            field=models.CharField(default='+5500000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tipo',
            field=models.CharField(choices=[('C', 'Cliente'), ('A', 'Administrador')], default='C', max_length=1),
        ),
    ]
