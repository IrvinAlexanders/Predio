
from django.urls import reverse_lazy
from django.views import generic
from .forms import Clienteform
from .models import Cliente

class Clienteview(generic.ListView):
    model = Cliente
    template_name = 'listcliente.html'
    context_object_name = 'cliente'
class Clienteinsertar(generic.CreateView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'formcliente.html'
    form_class = Clienteform
    success_url = reverse_lazy("Cliente:clientes")
   
class Clienteeditar(generic.UpdateView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'formcliente.html'
    form_class = Clienteform
    success_url = reverse_lazy("Cliente:clientes")

class Clienteeliminar(generic.DeleteView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'deletecliente.html'
    form_class = Clienteform
    success_url = reverse_lazy("Cliente:clientes")
   