from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
import uuid


STATUS = (
    ('Planejamento', 'Planejamento'),
    ('Execução', 'Execução'),
    ('Monitoramento', 'Monitoramento'),
    ('Concluído', 'Concluído'),
)
    

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return 'products/' + str(filename)


# Base
class Base(models.Model):
    created = models.DateField('Data de Criação', auto_now_add=True)
    modified = models.DateField('Data de Modificação', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True



# Serviços
class Service(Base):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', null=True)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name
    

# Projeto
class Project(Base):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    start_date = models.DateField('Data Inicial', null=True, blank=True)
    end_date = models.DateField('Data Final', null=True, blank=True)
    cost = models.DecimalField('Custo', max_digits=8, decimal_places=2)
    client = models.ForeignKey('accounts.CustomUser', verbose_name='Cliente', on_delete=models.CASCADE, limit_choices_to={'level': 'client'})
    service = models.ForeignKey('core.Service', verbose_name='Serviços', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=20, choices=STATUS, default='Planejamento')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.name


# Pagamento
class Payment(Base):
    description = models.TextField('Descrição')
    cost = models.DecimalField('Custo', max_digits=8, decimal_places=2)
    project = models.ForeignKey('core.Project', verbose_name='Projeto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.project


class Message(Base):
    sender = models.ForeignKey(User, related_name='sent_messages', verbose_name='remetente', on_delete=models.CASCADE, null=True)
    addressee = models.ForeignKey(User, related_name='received_messages', verbose_name='destinatario', on_delete=models.CASCADE, null=True)
    content = models.TextField('conteúdo', null=True)
    read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.read = True
        self.save()
    



# Fatura
class Invoice(Base):
    name = models.CharField('Nome', max_length=100)
    detail = models.TextField('Detalhes')

