from django.shortcuts import render
from rest_framework import viewsets
from .models import Bill, InsuranceDetails
from .serializer import BillsSerializer, InsuranceDetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter




class InsuranceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InsuranceDetails.objects.all()
    serializer_class = InsuranceDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient','patient__user__username', 'company', 'number']

    