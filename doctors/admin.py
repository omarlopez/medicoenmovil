from django.contrib import admin
from .models import Doctors

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["created", "fullName", "lastName", "email", "cedProf", "isActive"]

admin.site.register(Doctors, DoctorsAdmin)