from django.urls import path , include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register('exams-list', ExamsListViewSet, basename='exams-list')
router.register('exam-request', ExamRequestViewSet, basename='exam-request')
router.register('radiology-results', RadiologyResultsViewSet, basename='radiology-results')
router.register('radiology-result-details', RadiologyResultDetailsViewSet, basename='radiology-result-details')
router.register('test-result', TestResultViewSet, basename='test-result')

urlpatterns = [

    path('', include(router.urls)),

]