from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS
from rest_framework import pagination
from rest_framework import exceptions
from rest_framework import filters
from .models import *
from .serializers import *




class ExamsListViewSet(ModelViewSet):
    queryset = ExamsList.objects.all()
    serializer_class = ExamsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    pagination_class = pagination.PageNumberPagination




class ExamRequestViewSet(ModelViewSet):
    queryset = ExamRequest.objects.prefetch_related('exams').select_related('patient__user','doctor__user').select_related('appointment').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'patient', 'doctor','exams__type']
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ExameRequestSerializer
        else: return CreateExameRequest



class RadiologyResultsViewSet(GenericViewSet):
    queryset = RadiologyResult.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request','Request__patient', 'exam']
    pagination_class = pagination.PageNumberPagination


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
           return RadiologyResultSerializer
        else: return CreateRadiologyResult


class RadiologyResultDetailsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = RadiologyResultDetails.objects.all()
    serializer_class = RadiolgyResultDetailsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['result']
    search_fields = ['comment']
    pagination_class = pagination.PageNumberPagination




class TestResultViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Request__patient','Request', 'exam']
    pagination_class = pagination.PageNumberPagination