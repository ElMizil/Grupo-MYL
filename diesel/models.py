from django.db import models
from django.utils import timezone
from decimal import Decimal

class DieselLog(models.Model):
    class Ubicacion(models.TextChoices):
        YARDA = "YARDA", "Yarda"
        OBRA = "OBRA", "Obra"
        DIAM = "DIAM", "Diam"

    ubicacion = models.CharField(max_length=20, choices=Ubicacion.choices)
    unidad = models.CharField(max_length=50)
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    operador = models.CharField(max_length=100)

    precio_por_litro = models.DecimalField(max_digits=10, decimal_places=4)
    costo_total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        # costo_total = litros * precio_por_litro
        self.costo_total = (self.litros or Decimal("0")) * (self.precio_por_litro or Decimal("0"))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.unidad} - {self.ubicacion} - {self.fecha:%Y-%m-%d %H:%M}"
