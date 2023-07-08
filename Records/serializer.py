from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from Hospital.serializer import *


class EmergencyContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EmergencyContact
        fields = ['id', 'first_name', 'last_name', 'email', 'gender',
                  'phone_1', 'phone_2', 'relative_relation', 'national_id', 'address']

    def create(self, validated_data):
        user = self.context['user']
        patient = Patient.objects.get(user=user)
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        return EmergencyContact.objects.create(patient_id=patient.id, address=address, **validated_data)

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = Address(**address_data)
        address.save()
        instance.address = address
        instance.save()
        return instance


class ReceptionistEmergencyContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EmergencyContact
        fields = ['id', 'patient', 'first_name', 'last_name', 'email', 'gender',
                  'phone_1', 'phone_2', 'relative_relation', 'national_id', 'address']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        return EmergencyContact.objects.create(address=address, **validated_data)

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = Address(**address_data)
        address.save()
        instance.address = address
        instance.save()
        return instance


class ViewSurgeryInfoSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = SurgeryInfo
        fields = ['patient', 'doctor', 'surgery_type',
                  'date', 'time', 'documentation']

    def get_patient(self, obj):
        patient = obj.patient
        return {
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name,
        }

    def get_doctor(self, obj):
        doctor = obj.doctor
        return {
            'id': doctor.id,
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name,
        }


class SurgeryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryInfo
        fields = ['patient', 'doctor', 'surgery_type',
                  'date', 'time', 'documentation']


class PatientSurgeryInfoSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = SurgeryInfo
        fields = ['doctor', 'surgery_type', 'date', 'time', 'documentation']

    def get_doctor(self, obj):
        doctor = obj.doctor
        return {
            'id': doctor.id,
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name,
        }


class DoctorSurgeryInfoSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = SurgeryInfo
        fields = ['patient', 'surgery_type', 'date', 'time', 'documentation']

    def get_patient(self, obj):
        patient = obj.patient
        return {
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name,
        }


class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ['id', 'patient', 'doctor', 'room_number', 'bed_number',
                  'admission_date', 'discharge_date', 'diagnosis', 'notes']


class ViewVisitSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = Visits
        fields = ['id', 'patient', 'doctor', 'diagnosis',
                  'admission_date', 'discharge_date']

    def get_patient(self, obj):
        patient = obj.patient
        return {
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name
        }

    def get_doctor(self, obj):
        doctor = obj.doctor
        return {
            'id': doctor.id,
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name
        }


class ViewVitalSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = Vitals
        fields = ['id', 'patient', 'date', 'time', 'height',
                  'weight', 'blood_pressure', 'heart_rate', 'temperature']

    def get_patient(self, obj):
        patient = obj.patient
        return {
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name
        }


class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = ['id', 'patient', 'date', 'time', 'height',
                  'weight', 'blood_pressure', 'heart_rate', 'temperature']


class PatientVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = ['id', 'date', 'time', 'height', 'weight',
                  'blood_pressure', 'heart_rate', 'temperature']


class ViewMedicalRecordSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = ['patient', 'diagnosis', 'allergies', 'family_history']

    def get_patient(self, obj):
        patient = obj.patient
        return {
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name
        }


class MedicalRecordSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'diagnosis', 'allergies', 'family_history']


class PatientMedicalRecordSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'allergies', 'family_history']


class PatientAllRecordrSerializer(serializers.ModelSerializer):
    medical_record = serializers.SerializerMethodField()
    vitals = serializers.SerializerMethodField()
    surgeries = serializers.SerializerMethodField()
    visits = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'medical_record', 'vitals', 'visits', 'surgeries']

    def get_vitals(self, obj):
        vitals = obj.patient_vital.all()
        if vitals.count() > 0:
            return VitalSerializer(vitals, many=True).data
        else:
            return ('This person has no vitals')

    def get_visits(self, obj):
        visits = obj.inpatient.all()
        if visits.count() > 0:
            return VisitsSerializer(visits, many=True).data
        else:
            return ('This person has no visits')

    def get_surgeries(self, obj):
        surgeries = obj.patient_surgery.all()
        if surgeries.count() > 0:
            return SurgeryInfoSerializer(surgeries, many=True).data
        else:
            return ('This person has no surgeries')

    def get_medical_record(self, obj):
        try:
            medical_record = obj.patient_record
            return MedicalRecordSerializer(medical_record).data
        except MedicalRecord.DoesNotExist:
            return ('This person has no medical record')
