from django.db import models
from datetime import date, datetime

class Enlace(models.Model):
    fecha_registro = models.DateField()
    descripcion =   models.CharField(max_length=120)
    enlace = models.CharField(max_length=100)

    def __str__(self):
        return self.enlace
