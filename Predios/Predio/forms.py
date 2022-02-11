from django import forms
from .models import Predio


class Predioform(forms.ModelForm):
    class Meta:
        model = Predio
        fields = ['Ubicacion','TipoGeografia']
        labels = {'Ubicacion': 'Digite la ubicacion ',
                  'TipoGeografia': 'Seleccione el tipo de geografia'
                 }
        widget = {'Ubicacion': forms.TextInput(),
                  'TipoGeografia': forms.TextInput(),
                 }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
