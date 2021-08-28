from django.db import models


class User(models.Model):
    class Meta:
        abstract = True
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Patient(User):
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    date_of_birth = models.DateField()


class Provider(User):
    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    patients = models.ManyToManyField(Patient, related_name='providers')


