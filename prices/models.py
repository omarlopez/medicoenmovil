from django.db import models

# Create your models here.
class Prices(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=100, verbose_name="Precio")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    isActive = models.BooleanField(verbose_name="Activo")

    class Meta:
        verbose_name_plural = "Precios"
    
