from django import forms
from .models import Cliente


class Clienteform(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['TipoIdentificacion','TipoCliente', 'NombreCliente','numeroIdentificacion']
        labels = {'TipoIdentificacion': 'Seleccione tipo de identificacion ',
                  'TipoCliente': 'Seleccione tipo de cliente  ',
                  'NombreCliente': 'Nombre del cliente ',
                  'numeroIdentificacion':'numero de identificacion'
                 }
        widget = {'TipoIdentificacion': forms.TextInput(),
                  'TipoCliente': forms.TextInput(),
                  'NombreCliente': forms.TextInput(),
                  'numeroIdentificacion': forms.TextInput(),
                  }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
