from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('drug', DrugViewSet, basename='drug')
router.register('doctor-prescription', DoctorPrescriptionViewSet, basename='doctor-prescription')
router.register('pharmacist-prescription', PharmacistPrescriptionViewSet, basename='pharmacist-prescription')
router.register('receptionist-prescription', ReceptionistPrescriptionViewSet, basename='receptionist-prescription')
router.register('pharmacist', PharmacistViewSet, basename='pharmacist')
router.register('prescriptionitems', PrescriptionItemsViewSet, basename='prescriptionitems')


urlpatterns = router.urls
