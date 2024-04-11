from django.db import models

class Doctors(models.Model):
    LIST_OPTIONS = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )
    created = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100, verbose_name="Nombres")
    lastName = models.CharField(max_length=100, verbose_name="Apellido paterno")
    secondLastName = models.CharField(max_length=100, verbose_name="Apellido materno")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    email = models.CharField(max_length=100, verbose_name="Correo")
    cedProf = models.CharField(max_length=100, verbose_name="Cédula profesional")
    genero = models.CharField(max_length=15, choices=LIST_OPTIONS, verbose_name="Genero")
    isActive = models.BooleanField(verbose_name="Activo")

    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name_plural = "Doctores"
    







