from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome=models.CharField(max_length=40)
    cpf=models.CharField(max_length=11)
    telefone=models.IntegerField()
    cep=models.IntegerField()
    rua=models.CharField(max_length=35)
    estado=models.CharField(max_length=10)
    cidade=models.CharField(max_length=15)
    uf=models.CharField(max_length=3)

class produto(models.Model):
    produto=models.CharField(max_length=40)
    valor=models.FloatField()
    quantidade=models.IntegerField()



