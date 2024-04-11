from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ["doctor", "status"]

admin.site.register(Activity, ActivityAdmin)
