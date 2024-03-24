from django.db import models

# Create your models here.
class Doctors(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    secondLastName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cedProf = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural = "Doctores"
    







