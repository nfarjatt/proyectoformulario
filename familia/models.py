from django.db import models
from concurrent.futures.process import _MAX_WINDOWS_WORKERS

class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    altura = models.FloatField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def calcular_edad(self):
        import datetime

        año_hoy = datetime.date.today().year
        return año_hoy - self.fecha_nacimiento.year