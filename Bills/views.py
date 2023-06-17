from django.shortcuts import render
from rest_framework import viewsets
from .models import Bill, InsuranceDetails
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import *

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class InsuranceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InsuranceDetails.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [CreateOrEditOrDeleteInsuranceDetails]
    search_fields = ['patient__user__username']
    filterset_fields = ['patient',
                        'patient__user__username', 'company', 'number']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return InsuranceDetailsSerializer
        else:
            return CreateInsuranceDetailsSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'patient':
            return InsuranceDetails.objects.filter(patient__user=user)
        elif user.role == 'receptionist':
            return InsuranceDetails.objects.all()
        else:
            return InsuranceDetails.objects.none()


class BillsViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [BillPermission]
    filterset_fields = ['patient', 'patient__user__username', 'appointment']
    search_fields = ['patient__user__first_name', 'patient__user__last_name',
                     'patient__user__national_id', 'patient__user__phone_1']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return BillsSerializer
        else:
            return CreateBillsSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'patient':
            return Bill.objects.select_related('patient__user', 'appointment', 'appointment__doctor__user', 'appointment__slot', 'appointment__slot__schedule', 'insurance', 'radiology_request', 'lab_request', 'prescription').filter(patient__user=user)
        elif user.role == 'receptionist':
            return Bill.objects.select_related('patient__user', 'appointment', 'appointment__doctor__user', 'appointment__slot', 'appointment__slot__schedule', 'insurance', 'radiology_request', 'lab_request', 'prescription').all()
        else:
            return Bill.objects.none()
