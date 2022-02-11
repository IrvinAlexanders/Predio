from django.db import models

from Clients.models import Cliente
# Create your models here.
class DetalleClientePersona(models.Model):
    edad = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.apellido)
class Meta:
      verbose_name_plural='TipoClientes'
