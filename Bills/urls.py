from rest_framework import routers
from django.urls import path, include
from .views import *



router = routers.DefaultRouter()
router.register('insurancedetails', InsuranceDetailsViewSet, basename='InsuranceDetails')
router.register('bill', BillsViewSet, basename='Bills')



urlpatterns = [

    path('', include(router.urls)),

]
