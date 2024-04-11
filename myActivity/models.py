from django.db import models
from statusCatalog.models import CatalogStatus
from doctors.models import Doctors
from django.contrib.auth.models import User

class MyActivity(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Doctor", default = None)
    status = models.ForeignKey(CatalogStatus, verbose_name=("Status"), on_delete=models.CASCADE, default = None)

    class Meta:
        verbose_name_plural = "Mi Actividad"