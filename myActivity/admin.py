from django.contrib import admin
from .models import MyActivity

class MyActivityAdmin(admin.ModelAdmin):
    list_display = ["doctor", "status"]

admin.site.register(MyActivity, MyActivityAdmin)

