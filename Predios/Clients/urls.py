
from django.urls import  path
from .views import Clienteview,Clienteinsertar,Clienteeditar,Clienteeliminar
urlpatterns = [
    path('', Clienteview.as_view(), name='clientes'),
    path('cliente/new/', Clienteinsertar.as_view(), name='Insertar'),
    path('cliente/Editar/<int:pk>', Clienteeditar.as_view(), name='Editar'),
    path('cliente/eliminar/<int:pk>', Clienteeliminar.as_view(), name='Eliminar'),
]
