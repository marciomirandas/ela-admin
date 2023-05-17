from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
import uuid


LEVEL = (
        ('client', 'Cliente'),
        ('worker', 'Funcionário'),
)


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return 'profile_image/' + str(filename)


class Base(models.Model):
    created = models.DateField('Data de Criação', auto_now_add=True)
    modified = models.DateField('Data de Modificação', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# Usuários
class CustomUser(Base):
    name = models.CharField('Nome', max_length=100, null=True)
    user = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
    level = models.CharField('Nível', max_length=10, choices=LEVEL, default='client')
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.level


class Worker(Base):
    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE)
    phone = models.CharField('Telefone', max_length=20)
    address = models.CharField('Endereço', max_length=200)
    department = models.CharField('Departamento', max_length=100)
    office = models.CharField('Cargo', max_length=100)
    registration = models.CharField('Matrícula', max_length=20)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.phone
    

class Client(Base):
    user = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
    phone = models.CharField('Telefone', max_length=20)
    address = models.CharField('Endereço', max_length=200)
    cpf_cnpj = models.CharField(max_length=20)
    
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.user.username
