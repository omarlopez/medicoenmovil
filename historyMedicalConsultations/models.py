from django.db import models

class HistoryMedicalConsultations(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    doctor = models.CharField(max_length=50, verbose_name="Médico")
    date_start = models.CharField(max_length=50, verbose_name="Fecha - Hora/inicio consulta")
    date_end = models.CharField(max_length=50, verbose_name="Fecha - Hora/Termino consulta")
    incidents = models.CharField(max_length=50, verbose_name="Incidencias")
    user = models.CharField(max_length=50, verbose_name="Paciente")

    class Meta:
        verbose_name_plural = "Consultas del dia"