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


class InsuranceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InsuranceDetails.objects.all()
    filter_backends = [DjangoFilterBackend]
    permission_classes = [CreateOrEditOrDeleteInsuranceDetails]
    filterset_fields = ['patient','patient__user__username', 'company', 'number']


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateInsuranceDetailsSerializer
        return InsuranceDetailsSerializer
    

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
    filterset_fields = ['patient','patient__user__username', 'appointment']
    search_fields = ['patient__user__username']


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBillsSerializer
        return BillsSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'patient':
            return Bill.objects.filter(patient__user=user)
        elif user.role == 'receptionist':
            return Bill.objects.all()
        else:
            return Bill.objects.none()
    

    