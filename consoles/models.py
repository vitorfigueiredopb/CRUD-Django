from django.db import models

class Console(models.Model):
    consoleName = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    lancamento = models.IntegerField()
    descricao = models.CharField(max_length=200)