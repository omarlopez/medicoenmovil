from django.db import models

# Create your models here.
class Prices(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural = "Precios"
    
