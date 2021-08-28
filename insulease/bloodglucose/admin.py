from django.contrib import admin
from .models import BloodGlucose


@admin.register(BloodGlucose)
class BloodGlucoseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'patient', 'value', 'timestamp']
