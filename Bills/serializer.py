from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from django.contrib.auth.models import User
from Hospital.models import Patient, Doctor
from Lab_Radiology.models import ExamRequest
from Appointments.models import *
from .models import Bill, InsuranceDetails
from Lab_Radiology.models import ExamRequest, ExamsList
from Pharmacy.models import PrescriptionItems, Prescription
from pprint import pprint


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
        fields = ['id', 'dateTime', 'status', 'exams']


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = ['price']


class SlotSerializer(ModelSerializer):
    schedule = ScheduleSerializer()

    class Meta:
        model = Slot
        fields = ['id', 'start_time', 'schedule']


class AppointmentsSerializer(ModelSerializer):
    doctor = DoctorSerializer()
    slot = SlotSerializer()

    class Meta:
        model = BookedAppointment
        fields = ['id', 'date', 'doctor', 'slot']


class InsuranceDetailsSerializer(ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = InsuranceDetails
        fields = ['id', 'patient', 'company', 'number', 'expairy_date',
                  'coverage', 'coverage_percentage', 'card']


class CreateInsuranceDetailsSerializer(ModelSerializer):
    class Meta:
        model = InsuranceDetails
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        role = user.role
        if role == 'patient':
            patient_id = validated_data['patient'].id
            patient = Patient.objects.get(id=patient_id)
            if patient.user != user:
                raise serializers.ValidationError(
                    "You are not allowed to create insurance details for other patients")
            else:
                return InsuranceDetails.objects.create(**validated_data)
        elif role == 'receptionist':
            return InsuranceDetails.objects.create(**validated_data)


class PrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.SerializerMethodField()

    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'dispensed']

    def get_drug(self, obj):
        drug = obj.drug
        return {
            'name': drug.name,
            'price': drug.price,
        }


class PrescriptionSerializer(serializers.ModelSerializer):
    prescription = PrescriptionItemsSerializer(many=True)

    class Meta:
        model = Prescription
        fields = ['id', 'date', 'notes', 'dispensed_status',
                  'dispensed_by', 'prescription']
        read_only_fields = ['date', 'notes']


class BillsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    insurance = InsuranceDetailsSerializer()
    appointment = AppointmentsSerializer()
    radiology_request = ExamRequestSerializer()
    lab_request = ExamRequestSerializer()
    prescription = PrescriptionSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'patient', 'appointment', 'radiology_request',
                  'lab_request', 'prescription', 'insurance', 'time_date', 'total', 'discount']


class CreateBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ['total']
