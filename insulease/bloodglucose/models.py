from django.db import models


class BloodGlucose(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey('users.Patient', on_delete=models.PROTECT, related_name='blood_glucose')
    value = models.IntegerField()

    def __str__(self):
        return f"{self.patient}: {self.timestamp}"
