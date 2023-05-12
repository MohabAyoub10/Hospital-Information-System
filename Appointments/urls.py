from django.urls import path , include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('doctor-schedule', DoctorScheduleViewSet, basename='doctor-schedule')
router.register('doctor-slots', DoctorSlotsViewSet, basename='doctor-slots')
router.register('Booked-Appointments', BookedAppoitnmentViewSet, basename='doctor_schedule')
router.register('Doctor-Appointments', DoctorAppointmentsDetailsViewSet, basename='doctor_appointments')
urlpatterns = [
    path('', include(router.urls)),
]

