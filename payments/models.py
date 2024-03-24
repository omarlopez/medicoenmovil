from django.db import models

# Create your models here.
class Payments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    doctor = models.CharField()
    medicalConsultations = models.CharField()
    commission = models.CharField()
    totalPayments = models.CharField()
    isActive = models.BooleanField()