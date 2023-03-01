from django.db import models
from django.conf import settings


class Vehiculo(models.Model):
    propietario = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=25)
    año = models.IntegerField()
    modelo = models.CharField(max_length=25)
    chasis = models.CharField(max_length=8)

class Multa(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    valor = models.FloatField()
    año = models.IntegerField()
    descripcion = models.TextField()
