from django.db import models
from django.conf import settings

from appRequisitoPrevioVehicular.encrypt_util import *

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)

class Vehiculo(models.Model):
    propietario = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=25)
    año = models.IntegerField()
    modelo = models.CharField(max_length=25)
    chasis = models.CharField(max_length=8)

    def get_vehiculo_by_placa(self, dato):
        lista_vehiculos = Vehiculo.objects.all()
        vehiculo1 = Vehiculo.objects.get(placa=dato)
        for vehiculo in lista_vehiculos:
            aux = vehiculo.placa
            if aux == dato:
                return vehiculo
        raise Vehiculo.DoesNotExist(
                "%s matching query does not exist." % Vehiculo._meta.object_name
            )


    def get_vehiculo_by_chasis(self, dato):
        lista_vehiculos = Vehiculo.objects.all()
        for vehiculo in lista_vehiculos:
            aux = vehiculo.chasis
            if aux == dato:
                return vehiculo
        raise Vehiculo.DoesNotExist(
                "%s matching query does not exist." % Vehiculo._meta.object_name
            )

class Multa(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    valor = models.FloatField()
    año = models.IntegerField()
    descripcion = models.TextField()

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Canton(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, related_name='cantones', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Agencia(models.Model):
    nombre = models.CharField(max_length=100)
    canton = models.ForeignKey(Canton, related_name='agencias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre