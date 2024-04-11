from django.contrib import admin
from .models import Payments

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ["created", "doctor", "numberMedicalConsultations", "commission", "totalPayments", "isActive"]

admin.site.register(Payments, PaymentsAdmin)
