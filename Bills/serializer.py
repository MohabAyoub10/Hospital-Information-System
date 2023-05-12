from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from django.contrib.auth.models import User
from Hospital.models import Patient, Doctor
from Lab_Radiology.models import ExamRequest
from Appointments.models import BookedAppointment
from .models import Bill, InsuranceDetails


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


class BillsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Bill
        fields = ['patient', 'insurance', 'appointment', 'time_date']