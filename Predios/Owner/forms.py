from django import forms
from .models import Propietario

class Propietarioform(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['Cliente','Predio']
        labels = {'Cliente': 'seleccione el cliente',
                  'Predio': 'Seleccionar el predio'
                 }
        widget = {'Cliente': forms.TextInput(),
                  'Predio': forms.TextInput(),
                 }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
