# Generated by Django 3.2 on 2023-05-12 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20230512_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('detail', models.TextField(verbose_name='Detalhes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('detail', models.TextField(verbose_name='Detalhes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('detail', models.TextField(verbose_name='Detalhes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Custo')),
                ('status', models.CharField(max_length=50, verbose_name='Staus')),
                ('client', models.ForeignKey(limit_choices_to={'level': 'client'}, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='Cliente')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.service', verbose_name='Serviços')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Custo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project', verbose_name='Projeto')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
    ]