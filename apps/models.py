from django.db import models



# Create your models here.
class Usuario(models.Model):
    nome_usuario = models.CharField('Nome do usuario', unique=True, max_length=100)
    email = models.EmailField('Email do usuario', max_length=254, unique=True)
    nomes = models.CharField('Nomes', max_length=200, blank=True, null=True)
    sobrenome = models.CharField('Sobrenome', max_length=200, blank=True, null=True)
    usuario_online = models.BooleanField(default=True) 
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'nome_usuario'
    REQUIRED_FIELDS = ['email','nomes','sobrenome']

    def __str__(self):
        return f'{self.nomes},{self.sobrenome}'
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_labbel):
        return True


    @property
    def is_staff(self):
        return self.admin


class produto(models.Model):
    produto=models.CharField(max_length=40)
    valor=models.FloatField()
    quantidade=models.IntegerField()
    



