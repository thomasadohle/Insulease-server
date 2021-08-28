from rest_framework import serializers
from .models import BloodGlucose


class BloodGlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGlucose
        fields = ('pk', 'timestamp', 'patient', 'value')
