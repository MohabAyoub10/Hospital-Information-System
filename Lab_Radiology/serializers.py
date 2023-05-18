from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework import serializers
from Hospital.models import Patient, Doctor
from Appointments.models import BookedAppointment
from .models import *



class ExamsListSerializer(ModelSerializer):
    class Meta:
        model = ExamsList
        fields = '__all__'



class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user', 'first_name', 'last_name','specialty']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = BookedAppointment
        fields = ['id', 'date']



class ExameRequestSerializer(ModelSerializer):

    exams = ExamsListSerializer(many=True)
    appointment = AppointmentSerializer()
    
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = ExamRequest
        fields = ['id', 'appointment',  'exams','status', 'comment', 'patient', 'doctor']



class CreateExameRequest(ModelSerializer):

    class Meta:
        model = ExamRequest
        fields = '__all__'


class RadiolgyResultDetailsSerializer(ModelSerializer):
    class Meta:
        model = RadiologyResultDetails
        fields = '__all__'





class RadiologyResultSerializer(ModelSerializer):
    radiology_result = RadiolgyResultDetailsSerializer(many=True)
    exam = ExamsListSerializer()
    class Meta:
        model = RadiologyResult
        fields = ['id', 'exam', 'radiology_result']


class CreateRadiologyResult(ModelSerializer):
    class Meta:
        model = RadiologyResult
        fields = '__all__'


class TestResultSerializer(ModelSerializer):
    exam = ExamsListSerializer()
    class Meta:
        model = TestResult
        fields = ['Request', 'exam', 'dateTime', 'pdf_result', 'comment']


class TestResultByRequestSerializer(ModelSerializer):
    Lab_request = TestResultSerializer(many=True)
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = ExamRequest
        fields = ['id', 'Lab_request', 'patient', 'doctor',]

class CreateTestResult(ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'


class LabStaffSerializer(ModelSerializer):
    class Meta:
        model = LabStaff
        fields = ['id','user']


class RadiologyStaffSerializer(ModelSerializer):
    class Meta:
        model = RadiologyStaff
        fields = ['id','user']