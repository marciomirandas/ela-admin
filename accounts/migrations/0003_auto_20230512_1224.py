# Generated by Django 3.2 on 2023-05-12 15:24

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_customuser_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('department', models.CharField(max_length=100, verbose_name='Departamento')),
                ('office', models.CharField(max_length=100, verbose_name='Cargo')),
                ('registration', models.CharField(max_length=20, verbose_name='Matrícula')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to=accounts.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfies',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
