
from django.db import models
from GeographType.models import TipoGeografia
class Predio(models.Model):
    Ubicacion = models.CharField(max_length=200)
    TipoGeografia = models.ForeignKey(TipoGeografia, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Ubicacion)
class Meta:
      verbose_name_plural='Predios'
