from .models import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import *
from Hospital.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class EmergencyContactViewSet(ModelViewSet):
    serializer_class = EmergencyContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name']
    permission_classes = [IsPatientOrReadOnly]
    def get_queryset(self):
        if self.request.user.role=='patient':
            return EmergencyContact.objects.filter(patient__user=self.request.user).select_related('address').all()
        return EmergencyContact.objects.select_related('address').all()
    def get_serializer_class(self):
        if self.request.user.role == 'patient':
            return EmergencyContactSerializer
        return ReceptionistEmergencyContactSerializer
    def get_serializer_context(self):
        return {'user':self.request.user}




     
class VisitViewSet(ModelViewSet):
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['admission_date','discharge_date']
    search_fields = ['doctor__user__first_name','doctor__user__last_name','patient__user__first_name','patient__user__last_name']
    serializer_class = VisitsSerializer
    permission_classes = [IsMedicalSecretaryOrPatientDoctorReadOnly]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ViewVisitSerializer
        return VisitsSerializer
    def get_queryset(self):
        if self.request.user.role == 'patient':
            return Visits.objects.select_related('patient__user').select_related('doctor__user').filter(patient__user=self.request.user).all()
        elif self.request.user.role == 'doctor':
            return Visits.objects.select_related('patient__user').select_related('doctor__user').filter(doctor__user=self.request.user).all()
        return Visits.objects.select_related('patient__user').select_related('doctor__user').all() 

    
class SurgeryViewSet(ModelViewSet):
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['surgery_type','doctor']
    search_fields = ['doctor__user__first_name','doctor__user__last_name','patient__user__first_name','patient__user__last_name','surgery_type']
    permission_classes = [IsMedicalSecretaryOrPatientDoctorReadOnly]
    def get_serializer_class(self):
        if self.request.user.role == 'patient':
            return PatientSurgeryInfoSerializer
        elif self.request.user.role == 'doctor':
            return DoctorSurgeryInfoSerializer
        return SurgeryInfoSerializer
    def get_queryset(self):
        if self.request.user.role == 'patient':
            return SurgeryInfo.objects.filter(patient__user=self.request.user).select_related('patient__user').select_related('doctor__user').all()
        elif self.request.user.role == 'doctor':
            return SurgeryInfo.objects.filter(doctor__user=self.request.user).select_related('patient__user').select_related('doctor__user').all()
        return  SurgeryInfo.objects.select_related('patient__user').select_related('patient__user').all()




class VitalViewSet(ModelViewSet):
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['patient','date']
    search_fields = ['patient__user__first_name','patient__user__last_name']
    permission_classes = [IsMedicalSecretaryOrPatientReadOnly] 
    def get_serializer_class(self):
        if self.request.user.role == 'patient':
            return PatientVitalSerializer
        return VitalSerializer
    def get_queryset(self):
        if self.request.user.role == 'patient':
            return Vitals.objects.select_related('patient__user').filter(patient__user=self.request.user).all()
        return Vitals.objects.select_related('patient__user').all()
    


class MedicalRecordViewSet(ModelViewSet):
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['patient']
    search_fields = ['patient__user__first_name','patient__user__last_name']
    permission_classes = [IsMedicalSecretaryOrPatientDoctorReadOnly]
    def get_serializer_class(self):
        if self.request.user.role == 'patient':
            return PatientMedicalRecordSerializer
        return MedicalRecordSerializer
    def get_queryset(self):
        if self.request.user.role == 'patient':
            return MedicalRecord.objects.filter(patient__user=self.request.user).select_related('patient__user').all()
        return MedicalRecord.objects.select_related('patient').select_related('patient__user').all()

     

class PatientRecordsViewSet(ReadOnlyModelViewSet):
    queryset = Patient.objects.select_related('patient_record').prefetch_related('patient_vital').prefetch_related('patient_surgery').prefetch_related('patient_surgery').prefetch_related('inpatient').all()
    serializer_class = PatientAllRecordrSerializer
     

