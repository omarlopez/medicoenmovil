from django.contrib import admin
from .models import Doctors

# Register your models here.
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["created", "fullName", "lastName", "email", "cedProf"]

admin.site.register(Doctors, DoctorsAdmin)