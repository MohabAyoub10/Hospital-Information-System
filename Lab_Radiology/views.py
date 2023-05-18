from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework import exceptions
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from .models import *
from .permissions import *
from .serializers import *
from .custom_viewset import CustomModelViewSet





class ExamsListViewSet(ModelViewSet):
    queryset = ExamsList.objects.all()
    permission_classes = [ViewOrCreatOrEditExams]
    serializer_class = ExamsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    pagination_class = pagination.PageNumberPagination




class ExamRequestViewSet(ModelViewSet):
    queryset = ExamRequest.objects.prefetch_related('exams').select_related('appointment','patient__user','doctor__user').all()
    permission_classes = [CanViewOrEdit]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'patient', 'doctor','exams__type']
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ExameRequestSerializer
        else: return CreateExameRequest




class RadiologyResultsViewSet(ModelViewSet):
    queryset = RadiologyResult.objects.select_related('Request','Request__patient__user','Request__doctor__user').select_related('Request__appointment').select_related('exam').prefetch_related('Request__exams').prefetch_related('radiology_result').all()
    permission_classes = [CanViewOrEditOrCreatRadiologyResult]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request','Request__patient', 'exam']
    pagination_class = pagination.PageNumberPagination


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
           return RadiologyResultSerializer
        else: return CreateRadiologyResult


class RadiologyResultDetailsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = RadiologyResultDetails.objects.select_related('result').all()
    permission_classes = [CanViewOrEditOrCreatRadiologyResult]
    serializer_class = RadiolgyResultDetailsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['result']
    search_fields = ['comment']
    pagination_class = pagination.PageNumberPagination




class TestResultViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = TestResult.objects.all()
    permission_classes = [CanViewOrEditOrCreatLabResult]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request__patient','Request', 'exam']
    pagination_class = pagination.PageNumberPagination


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
           return TestResultSerializer
        else: return CreateTestResult


class RadiologyStaffViewSet(CustomModelViewSet):
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name','user__last_name']
    queryset = RadiologyStaff.objects.select_related('user').all()
    serializer_class = RadiologyStaffSerializer


class LabStaffViewSet(CustomModelViewSet):
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name','user__last_name']
    queryset = LabStaff.objects.select_related('user').all()
    serializer_class = LabStaffSerializer


class TestResutlByRequestViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = ExamRequest.objects.prefetch_related('exams','Lab_request','Lab_request__exam').select_related('appointment','patient__user','doctor__user',).filter(status='Completed')
    serializer_class = TestResultByRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'patient', 'doctor','exams__type']
    pagination_class = pagination.PageNumberPagination

    