from django.db import models
from Hospital.models import *
from phonenumber_field.modelfields import PhoneNumberField


class EmergencyContact(models.Model):
    genders = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    relatives = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Cousin', 'Cousin'),
        ('Sister', 'Sister'),
        ('Brother', 'Brother'),
        ('Aunt', 'Aunt'),
        ('Uncle', 'Uncle'),
        ('Grandfather', 'Grandfather'),
        ('Grandmother', 'Grandmother'),
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
        ('Others', 'Others')
    ]
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_emergency_conact')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=1, blank=1, null=1)
    gender = models.CharField(max_length=1, choices=genders)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=1, null=1)
    relative_relation = models.CharField(max_length=12, choices=relatives)
    national_id = models.CharField(max_length=14, unique=1)
    address = models.ForeignKey(
        Address, related_name='emergency_contact_address', on_delete=models.CASCADE, null=1, blank=1)

    def __str__(self) -> str:
        try:
            return str(self.first_name+' '+self.last_name)
        except Patient.DoesNotExist:
            pass
    # national-id , phone2


class SurgeryInfo(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_surgery')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.PROTECT, related_name='surgeon')
    surgery_type = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    documentation = models.FileField(upload_to='Records/surgeries')

    def __str__(self) -> str:
        try:
            return str(self.patient.user.first_name+' '+self.patient.user.last_name)
        except Patient.DoesNotExist:
            pass


class Visits(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='inpatient')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.PROTECT, related_name='patient_doctor')
    # nurse = models.ForeignKey(Nurse,on_delete=models.PROTECT,related_name='patient_nurse')
    room_number = models.PositiveSmallIntegerField()
    bed_number = models.PositiveSmallIntegerField()
    admission_date = models.DateField()
    discharge_date = models.DateField()
    diagnosis = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self) -> str:
        try:
            return str(self.patient.user.first_name+' '+self.patient.user.last_name)
        except Patient.DoesNotExist:
            pass


class Vitals(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_vital')
    date = models.DateField()
    time = models.TimeField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    blood_pressure = models.PositiveSmallIntegerField()
    heart_rate = models.PositiveSmallIntegerField()
    temperature = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        try:
            return str(self.patient.user.first_name+' '+self.patient.user.last_name)
        except Patient.DoesNotExist:
            pass


class MedicalRecord(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, primary_key=1, related_name='patient_record')
    diagnosis = models.TextField()
    allergies = models.TextField()
    family_history = models.TextField()

    def __str__(self) -> str:
        try:
            return str(self.patient.user.first_name+' '+self.patient.user.last_name)
        except Patient.DoesNotExist:
            pass
