from django.db import models
from django.conf import settings


class Vehiculo(models.Model):
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=25)
    año = models.IntegerField()
    modelo = models.CharField(max_length=25)
    chasis = models.CharField(max_length=8)


