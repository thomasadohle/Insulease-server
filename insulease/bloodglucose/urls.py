from .views import BloodGlucoseViewset
from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path


router = routers.DefaultRouter()
router.register(r'blood-glucose', BloodGlucoseViewset)

urlpatterns = [
    path(r'^', include(router.urls))
]