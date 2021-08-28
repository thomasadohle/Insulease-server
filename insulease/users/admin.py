from django.contrib import admin
from .models import Patient, Provider


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    fields = ['username', 'first_name', 'last_name']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    fields = ['username', 'first_name', 'last_name']
