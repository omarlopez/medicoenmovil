from django.db import models

# Create your models here.
class UserConsul(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    lastName = models.CharField()
    ciudad = models.CharField()
    email = model.CharField()
    genero = model.CharField()
    isActive = models.BooleanField()