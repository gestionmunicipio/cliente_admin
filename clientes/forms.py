from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Direccion
from django.utils.translation import gettext_lazy as _

class DireccionForm(forms.ModelForm):
#    class Meta:
#        model = Direccion
#       # fields = '__all__'
#        fields = ['calle', 'region', 'ciudad', 'codigo_postal']
    class Meta:
        model = Direccion
        fields = ['calle', 'region', 'ciudad', 'codigo_postal']
        labels = {
            'calle': _('Calle'),
            'region': _('Región'),
            'ciudad': _('Ciudad'),
            'codigo_postal': _('Código Postal'),
        }        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

DireccionFormSet = inlineformset_factory(
    Cliente, Direccion,
    fields=['calle', 'ciudad', 'region', 'codigo_postal'],
    extra=1,
    can_delete=True
)