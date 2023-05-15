from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from django.contrib.auth.models import User
from Hospital.models import Patient, Doctor
from Lab_Radiology.models import ExamRequest
from Appointments.models import BookedAppointment
from .models import Bill, InsuranceDetails
from Lab_Radiology.models import ExamRequest, ExamsList

class PatientSerializer(ModelSerializer):
    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name']


class DoctorSerializer(ModelSerializer):
    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'first_name', 'last_name', 'specialty']


class ExamListSerializer(ModelSerializer):

    class Meta:
        model = ExamsList
        fields = ['name', 'price']


class ExamRequestSerializer(ModelSerializer):
    exams = ExamListSerializer(many=True)

    class Meta:
        model = ExamRequest
        fields = ['id','dateTime', 'status', 'exams']
class AppointmentsSerializer(ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = BookedAppointment
        fields = ['id', 'date', 'doctor']


class InsuranceDetailsSerializer(ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = InsuranceDetails
        fields = ['patient', 'company', 'number', 'expairy_date', 'coverage', 'coverage_percentage', 'card']
        

class CreateInsuranceDetailsSerializer(ModelSerializer):
    class Meta:
        model = InsuranceDetails
        fields = '__all__'


class BillsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    insurance = InsuranceDetailsSerializer()
    appointment = AppointmentsSerializer()
    examrequest = ExamRequestSerializer()
    class Meta:
        model = Bill
        fields = ['patient', 'appointment', 'examrequest','insurance','time_date', 'total']


class CreateBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ['total']