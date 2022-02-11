from django.urls import  path
from .views import Predioview,Predioinsertar,Predioeditar,Predioeliminar
urlpatterns = [
    path('', Predioview.as_view(), name='predios'),
    path('predio/new/', Predioinsertar.as_view(), name='Insertar'),
    path('Predio/Editar/<int:pk>', Predioeditar.as_view(), name='Editar'),
    path('predio/eliminar/<int:pk>', Predioeliminar.as_view(), name='Eliminar'),
]
