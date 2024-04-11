from django.db import models
from doctors.models import Doctors
from statusCatalog.models import CatalogStatus

class Activity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    doctor = models.OneToOneField(Doctors, verbose_name=("Doctor"), on_delete=models.CASCADE)
    status = models.OneToOneField(CatalogStatus, verbose_name=("status"), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actividad"