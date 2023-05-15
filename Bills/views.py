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




class InsuranceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InsuranceDetails.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient','patient__user__username', 'company', 'number']


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateInsuranceDetailsSerializer
        return InsuranceDetailsSerializer
    


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['patient','patient__user__username', 'appointment']
    search_fields = ['patient__user__username']


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBillsSerializer
        return BillsSerializer



    

    