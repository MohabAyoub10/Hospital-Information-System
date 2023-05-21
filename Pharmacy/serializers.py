from rest_framework import serializers
from .models import *
from Core.models import User


class PharmacistDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class ViewerDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'name', 'price', 'stock', 'form']
class PharmacistSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Pharmacist
        fields = ['id', 'name', 'user','license', ]
        read_only_fields = ['user']
    def get_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

class PostPrescriptionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'prescription']


class PrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.StringRelatedField()
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'dispensed' ]

class ReceptionPrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.SerializerMethodField()
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'dispensed']
    
    def get_drug(self, obj):
        drug= obj.drug 
        return {
        'name': drug.name,
        'price': drug.price,
        }


class DoctorViewPrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.StringRelatedField()
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration']

class DoctorPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    class Meta:
        model = Prescription
        fields = ['id', 'patient','date', 'notes', 'prescription' ,'appointment']
    
    def create(self, validated_data):
        doctor_id = self.context['doctor_id']
        patient_id = validated_data.pop('patient')
        doctor =Doctor.objects.get(pk=doctor_id)
        prescription = Prescription.objects.create(doctor=doctor, patient=patient_id, **validated_data)
        return prescription


class DoctorViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    class Meta:
        model = Prescription
        fields = ['id', 'patient','doctor','date', 'notes', 'prescription','appointment' ]
        read_only_fields = ['patient','doctor','date', 'notes', 'prescription' ]
    def get_patient(self, obj):
        patient= obj.patient 
        return {
        'first_name': patient.user.first_name,
        'last_name': patient.user.last_name
        }
    def get_doctor(self, obj):
        doctor= obj.doctor 
        return {
        'first_name': doctor.user.first_name,
        'last_name': doctor.user.last_name
        }

class PharmacistPrescriptionSerializer(serializers.ModelSerializer):
    prescription = PrescriptionItemsSerializer(many=True, read_only=True)
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_status','dispensed_by', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes','dispensed_by']

    def update(self, instance, validated_data):
        pharmacist = Pharmacist.objects.get(pk = self.context['pharmacist_id'])
        instance.dispensed_by = pharmacist
        instance.dispensed_status = validated_data.get('dispensed_status', instance.dispensed_status)
        instance.save()
        return instance
    def get_patient(self, obj):
        patient= obj.patient 
        return {
        'first_name': patient.user.first_name,
        'last_name': patient.user.last_name
        }
    def get_doctor(self, obj):
        doctor= obj.doctor 
        return {
        'first_name': doctor.user.first_name,
        'last_name': doctor.user.last_name
        }

class PharmacistViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = PrescriptionItemsSerializer(many=True, read_only=True)
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_status','dispensed_by', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']
    def get_patient(self, obj):
        patient= obj.patient 
        return {
        'first_name': patient.user.first_name,
        'last_name': patient.user.last_name
        }
    def get_doctor(self, obj):
        doctor= obj.doctor 
        return {
        'first_name': doctor.user.first_name,
        'last_name': doctor.user.last_name
        }

class ReceptionistDispensingPrescriptionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'prescription', 'dispensed', ]

class ReceptionistViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = ReceptionPrescriptionItemsSerializer(many=True)
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_status','dispensed_by', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']
    def get_patient(self, obj):
        patient= obj.patient 
        return {
        'first_name': patient.user.first_name,
        'last_name': patient.user.last_name
        }
    def get_doctor(self, obj):
        doctor= obj.doctor 
        return {
        'first_name': doctor.user.first_name,
        'last_name': doctor.user.last_name
        }

class ReceptionistPrescriptionSerializer(serializers.ModelSerializer):
    prescription = ReceptionistDispensingPrescriptionItemsSerializer(many=True)
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_status', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']


    def create(self, validated_data):
        prescription_items_data = validated_data.pop('prescription', [])
        prescription = Prescription.objects.create(**validated_data)

        for item_data in prescription_items_data:
            PrescriptionItems.objects.create(prescription=prescription, **item_data)

        return prescription
    def update(self, instance, validated_data):
        prescription_items_data = validated_data.pop('prescription', [])
        prescription_items = instance.prescription.all()
        prescription_items_ids = [i.id for i in prescription_items]

        instance.doctor = validated_data.get('doctor', instance.doctor)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.date = validated_data.get('date', instance.date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.dispensed_status = validated_data.get('dispensed_status', instance.dispensed_status)
        instance.save()

        for item_data in prescription_items_data:
            item_id = item_data.get('id', None)
            if item_id in prescription_items_ids:
                item = prescription_items.get(id=item_id)
                item.drug = item_data.get('drug', item.drug)
                item.dose = item_data.get('dose', item.dose)
                item.duration = item_data.get('duration', item.duration)
                item.amount = item_data.get('amount', item.amount)
                item.dispensed = item_data.get('dispensed', item.dispensed)
                item.save()
            else:
                PrescriptionItems.objects.create(**item_data)

        for item in prescription_items:
            if item.id not in [i.get('id') for i in prescription_items_data]:
                item.delete()

        return instance

