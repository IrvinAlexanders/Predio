from django.db import models

class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)

class Meta:
      verbose_name_plural='IdType'
