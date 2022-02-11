from django.urls import reverse_lazy
from django.views import generic
from .forms import Predioform
from .models import Predio

class Predioview(generic.ListView):
    model = Predio
    template_name = 'listpredio.html'
    context_object_name = 'predio'
class Predioinsertar(generic.CreateView):
    model = Predio
    context_object_name = 'predio'
    template_name = 'formpredio.html'
    form_class = Predioform
    success_url = reverse_lazy("Predio:predios")
   
class Predioeditar(generic.UpdateView):
    model = Predio
    context_object_name = 'predio'
    template_name = 'formpredio.html'
    form_class = Predioform
    success_url = reverse_lazy("Predio:predios")

class Predioeliminar(generic.DeleteView):
    model = Predio
    context_object_name = 'predio'
    template_name = 'deletepredio.html'
    form_class = Predioform
    success_url = reverse_lazy("Predio:predios")
   
