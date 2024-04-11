from django.db import models
from doctors.models import Doctors

class Payments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name="Médico")
    numberMedicalConsultations = models.IntegerField(verbose_name="Número de consultas")
    commission = models.IntegerField(verbose_name="Comisiones")
    totalPayments = models.IntegerField(verbose_name="Total a pagar")
    isActive = models.BooleanField(verbose_name="Activo")

    class Meta:
        verbose_name_plural = "Pagos"