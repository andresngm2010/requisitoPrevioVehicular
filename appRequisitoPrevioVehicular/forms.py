from django import forms

from .models import Vehiculo, Multa

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('propietario', 'placa', 'marca', 'año', 'modelo', 'chasis')


class MultaForm(forms.ModelForm):

    class Meta:
        model = Multa
        fields = ('valor', 'año', 'descripcion')
