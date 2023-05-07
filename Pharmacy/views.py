from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Pharmacy.pagination import CustomPagination
from Pharmacy.permissions import *
from Pharmacy.custom_viewsets import *

class DrugViewSet(ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsPharmacistOrReadonly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['company', 'form', 'stock']
    search_fields = ['name', 'company', 'form']
    queryset = Drug.objects.all()
    def get_serializer_class(self):
        if self.request.user.role == 'pharmacist':
            return PharmacistDrugSerializer
        else:
            return ViewerDrugSerializer

class PharmacistViewSet(ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsAdminOrReadonly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['license']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'license']
    queryset = Pharmacist.objects.select_related('user').all()
    serializer_class = PharmacistSerializer

class PrescriptionItemsViewSet(ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsDoctorOrReadonly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['dispensed']
    search_fields = ['drug__name']
    queryset = PrescriptionItems.objects.all()
    def get_serializer_class(self):
        if self.request.user.role == 'doctor' and self.request.method == 'POST':
            return DoctorPrescriptionItemsSerializer
        else:
            return DispensingPrescriptionItemsSerializer
    def get_serializer_context(self):
        return {'user_id': 1} 
    # !! change after migrate with main Project to get profile doctor id or user id


# doctor and pharmacist and receptionist
# doctor for view and create
# pharmacist for dispensed by and dispensed confirm and view
# receptionist for update dispensed status

class DoctorPrescriptionViewSet(ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsDoctorOrReadonly]
    queryset = Prescription.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return DoctorPrescriptionSerializer
        else:
            return DoctorViewerPrescriptionSerializer
    def get_serializer_context(self):
        return {'user_id': 1}


class PharmacistPrescriptionViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsPharmacistOrReadonly]
    queryset = Prescription.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return PharmacistPrescriptionSerializer
        else:
            return PharmacistViewerPrescriptionSerializer
    def get_serializer_context(self):
        return {'user_id': 1}


class ReceptionistPrescriptionViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsReceptionistOrReadonly]
    queryset = Prescription.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return ReceptionistPrescriptionSerializer
        else:
            return ReceptionistViewerPrescriptionSerializer
    def get_serializer_context(self):
        return {'user_id': 1}