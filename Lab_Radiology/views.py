from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework import exceptions
from rest_framework import filters
from .models import *
from .permissions import *
from .serializers import *




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
    queryset = RadiologyResult.objects.select_related('Request','Request__patient__user','Request__doctor__user').select_related('Request__appointment').select_related('exam').prefetch_related('Request__exams').all()
    permission_classes = [CanViewOrEditOrCreatRadiologyResult]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request','Request__patient', 'exam']
    pagination_class = pagination.PageNumberPagination


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
           return RadiologyResultSerializer
        else: return CreateRadiologyResult


class RadiologyResultDetailsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = RadiologyResultDetails.objects.prefetch_related('radiology_result').all()
    permission_classes = [CanViewOrEditOrCreatRadiologyResult]
    serializer_class = RadiolgyResultDetailsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['result']
    search_fields = ['comment']
    pagination_class = pagination.PageNumberPagination




class TestResultViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = TestResult.objects.all()
    permission_classes = [CanViewOrEditOrCreatLabResult]
    serializer_class = TestResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request__patient','Request', 'exam']
    pagination_class = pagination.PageNumberPagination