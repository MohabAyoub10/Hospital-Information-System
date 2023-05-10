from rest_framework import serializers
from Hospital.models import Doctor, Specialty
from .models import *


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
    
    


    

class DoctorSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id','start_time','end_time','schedule']




class BookedAppoitnmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BookedAppointment
        fields = ['id','patient','doctor','slot','date','type','status']