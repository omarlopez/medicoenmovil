from django.db import models

# Create your models here.
class MedicalConsul(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nameDoctor = models.CharField(max_length=100)
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField()
    userPatient = model.CharField()