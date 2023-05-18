from django.urls import path , include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register('exams-list', ExamsListViewSet, basename='exams-list')
router.register('exam-request', ExamRequestViewSet, basename='exam-request')
router.register('radiology-results', RadiologyResultsViewSet, basename='radiology-results')
router.register('radiology-result-details', RadiologyResultDetailsViewSet, basename='radiology-result-details')
router.register('test-result', TestResultViewSet, basename='test-result')
router.register('view-test-resutls', TestResutlByRequestViewSet, basename='view-test-resutls')
router.register('view-radiology-request', RadiologyResultByRequestViewSet, basename='view-radiology-request')
router.register('lab-staff', LabStaffViewSet, basename='lab-staff')
router.register('radiology-staff', RadiologyStaffViewSet, basename='radiology-staff')

urlpatterns = [

    path('', include(router.urls)),

]