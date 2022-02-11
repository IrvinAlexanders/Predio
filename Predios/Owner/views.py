from django.urls import reverse_lazy
from django.views import generic
from .forms import Propietarioform
from .models import Propietario

class Propietarioview(generic.ListView):
    model = Propietario
    template_name = 'listpropietario.html'
    context_object_name = 'propietario'
class Propietarioinsertar(generic.CreateView):
    model = Propietario
    context_object_name = 'propietario'
    template_name = 'formpropietario.html'
    form_class = Propietarioform
    success_url = reverse_lazy("Propietario:propietarios")
   
class Propietarioeditar(generic.UpdateView):
    model = Propietario
    context_object_name = 'propietario'
    template_name = 'formpropietario.html'
    form_class = Propietarioform
    success_url = reverse_lazy("Propietario:propietarios")

class Propietarioeliminar(generic.DeleteView):
    model = Propietario
    context_object_name = 'propietario'
    template_name = 'deletepropietario.html'
    form_class = Propietarioform
    success_url = reverse_lazy("Propietario:propietarios")
