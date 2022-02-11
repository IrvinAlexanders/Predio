
from django.urls import reverse_lazy
from django.views import generic
from Owner.models import Propietario
from Clients.models import Cliente
from django.db.models import Q
#ilter(Cliente__numeroIdentificacion__icontains=query)
class search(generic.ListView):
    template_name = 'listconsulta.html'
    context_object_name = 'Propietario'
    def get_queryset(self):
        query = self.request.GET.get('name')
        if not query :
            query = ""
        return Propietario.objects.all().select_related('Cliente','Predio').filter(Q(Cliente__NombreCliente__startswith=query) | Q(Cliente__numeroIdentificacion__startswith=query) |  Q(Predio__TipoGeografia__nombre__startswith=query))