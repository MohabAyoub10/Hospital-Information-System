from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from Hospital.models import Doctor, Specialty
from .models import *


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user', 'first_name', 'last_name','specialty']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','user', 'first_name', 'last_name']

    user = StringRelatedField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = '__all__'


    def create(self, validated_data):
        doctor = validated_data.get('doctor')
        day = validated_data.get('day_of_week')
        if DoctorSchedule.objects.filter(doctor=doctor, day_of_week=day).exists():
            raise serializers.ValidationError({'Error': 'Doctor schedule already exists'})
        return super().create(validated_data)
    
    

class DoctorSchedulePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = ['id','price']
    

class DoctorSlotsSerializer(serializers.ModelSerializer):
    schedule = DoctorSchedulePriceSerializer()
    class Meta:
        model = Slot
        fields = ['id','start_time','end_time','schedule']




class BookedAppoitnmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    slot = DoctorSlotsSerializer()
    class Meta:
        model = BookedAppointment
        fields = ['id','patient','doctor','slot','date','type','status']


class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedAppointment
        fields = ['id','patient','doctor','slot','date','type','status']


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = DoctorAppointmentsDetails
        fields = ['id','doctor','schedule','date','total_appointments']