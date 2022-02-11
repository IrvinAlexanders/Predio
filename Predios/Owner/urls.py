from django.urls import  path
from .views import Propietarioview,Propietarioinsertar,Propietarioeditar,Propietarioeliminar
urlpatterns = [
    path('', Propietarioview.as_view(), name='propietarios'),
    path('propietario/new/', Propietarioinsertar.as_view(), name='Insertar'),
    path('propietario/Editar/<int:pk>', Propietarioeditar.as_view(), name='Editar'),
    path('propietario/eliminar/<int:pk>', Propietarioeliminar.as_view(), name='Eliminar'),
]
