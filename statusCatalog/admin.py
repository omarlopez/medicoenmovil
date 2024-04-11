from django.contrib import admin
from .models import CatalogStatus


class CatalogStatusAdmin(admin.ModelAdmin):
    list_display = ["created", "name", "description"]

admin.site.register(CatalogStatus, CatalogStatusAdmin)