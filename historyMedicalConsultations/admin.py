from django.contrib import admin
from .models import HistoryMedicalConsultations

class HistoryMedicalConsultationsAdmin(admin.ModelAdmin):
    list_display = ["created", "doctor", "date_start", "date_end", "incidents", "user"]

admin.site.register(HistoryMedicalConsultations, HistoryMedicalConsultationsAdmin)

