from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()
    
    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    cnpj = models.CharField(max_length=30)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField(default=False)
    imagem =models.FileField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE,  related_name='reservas_localizacao')
    
    
   