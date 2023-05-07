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

class DoctorPrescriptionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration']

    def create(self, validated_data):
        user_id = self.context['user_id']
        prescription = Prescription.objects.filter(doctor=user_id).last()
        prescription_items = PrescriptionItems.objects.create(prescription=prescription, **validated_data)
        return prescription_items

class DoctorViewPrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.StringRelatedField()
    prescription = serializers.StringRelatedField()
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'prescription',]

class DispensingPrescriptionItemsSerializer(serializers.ModelSerializer):
    drug = serializers.StringRelatedField()
    prescription = serializers.StringRelatedField()
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'prescription', 'dispensed', ]


class ReceptionistDispensingPrescriptionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItems
        fields = ['id', 'drug', 'amount', 'dose', 'duration', 'prescription', 'dispensed', ]


class DoctorViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    class Meta:
        model = Prescription
        fields = ['id', 'patient','doctor','date', 'notes', 'prescription' ]
        read_only_fields = ['patient','doctor','date', 'notes', 'prescription' ]

class DoctorPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    class Meta:
        model = Prescription
        fields = ['id', 'patient','date', 'notes', 'prescription' ]
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        patient_id = validated_data.pop('patient')
        doctor =User.objects.get(pk=user_id)
        prescription = Prescription.objects.create(doctor=doctor, patient=patient_id, **validated_data)
        return prescription


class PharmacistPrescriptionSerializer(serializers.ModelSerializer):
    prescription = serializers.SerializerMethodField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_confirm','prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']
    
    def get_prescription(self, obj):
        prescription_items = obj.prescription.filter(dispensed=True)
        serializer = DispensingPrescriptionItemsSerializer(prescription_items, many=True)
        return serializer.data

    def update(self, instance, validated_data):
        pharmacist = Pharmacist.objects.get(pk = self.context['user_id'])
        instance.dispensed_by = pharmacist
        instance.dispensed_confirm = validated_data.get('dispensed_confirm', instance.dispensed_confirm)
        return instance

class PharmacistViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    doctor = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'dispensed_confirm','dispensed_by', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']
class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'

class DoctorViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DoctorViewPrescriptionItemsSerializer(many=True, read_only=True)
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    class Meta:
        model = Prescription
        fields = ['id', 'patient','doctor','date', 'notes', 'prescription' ]
        read_only_fields = ['patient','doctor','date', 'notes', 'prescription' ]

class ReceptionistViewerPrescriptionSerializer(serializers.ModelSerializer):
    prescription = DispensingPrescriptionItemsSerializer(many=True)
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'prescription']
        read_only_fields = ['doctor', 'patient', 'date', 'notes']

class ReceptionistPrescriptionSerializer(serializers.ModelSerializer):
    prescription = ReceptionistDispensingPrescriptionItemsSerializer(many=True)
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date', 'notes', 'prescription']
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
                item.dispensed_by = item_data.get('dispensed_by', item.dispensed_by)
                item.save()
            else:
                PrescriptionItems.objects.create(**item_data)

        for item in prescription_items:
            if item.id not in [i.get('id') for i in prescription_items_data]:
                item.delete()

        return instance
