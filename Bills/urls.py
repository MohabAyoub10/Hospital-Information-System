from rest_framework import routers
from django.urls import path, include
from .views import InsuranceDetailsViewSet



router = routers.DefaultRouter()
router.register('InsuranceDetails', InsuranceDetailsViewSet, basename='InsuranceDetails')



urlpatterns = [

    path('', include(router.urls)),

]
