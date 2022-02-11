from django.db import models

# Create your models here.
from Clients.models import Cliente
from Predio.models import Predio
class Propietario(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Cliente)
class Meta:
      verbose_name_plural='Predios'

