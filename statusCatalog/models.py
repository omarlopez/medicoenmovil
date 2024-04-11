from django.db import models

class CatalogStatus(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name="Status")
    description = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Catalogo de status"

