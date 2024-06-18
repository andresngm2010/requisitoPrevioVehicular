from django import forms

from .models import Vehiculo, Multa, Usuario, Provincia, Canton, Agencia

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'cedula', 'telefono' )

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('propietario', 'placa', 'marca', 'año', 'modelo', 'chasis')


class MultaForm(forms.ModelForm):

    class Meta:
        model = Multa
        fields = ('valor', 'año', 'descripcion')


class UbicacionForm(forms.Form):
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all())
    canton = forms.ModelChoiceField(queryset=Canton.objects.none())
    agencia = forms.ModelChoiceField(queryset=Agencia.objects.none())


    class Media:
        js = ('js/carga_cantones.js',)  # Incluye el archivo JS en el formulario
