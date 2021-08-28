from django.shortcuts import render
from rest_framework import viewsets
from .models import BloodGlucose
from .serializers import BloodGlucoseSerializer


class BloodGlucoseViewset(viewsets.ModelViewSet):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodGlucoseSerializer




