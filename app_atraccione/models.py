from django.db import models

class Atraccione(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15)
    capacidad = models.IntegerField(default=1)
    estado = models.CharField(max_length=50, default='Operativa')
    altura_min = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Atraccione: {self.nombre} {self.tipo}'