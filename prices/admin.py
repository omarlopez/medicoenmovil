from django.contrib import admin
from .models import Prices


# Register your models here.
class PricesAdmin(admin.ModelAdmin):
    list_display = ["created", "price", "description", "isActive"]

admin.site.register(Prices, PricesAdmin)