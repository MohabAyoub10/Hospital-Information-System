from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    doctor = 'doctor'
    nurse = 'nurse'
    patient = 'patient'
    receptionist = 'receptionist'
    radiologist = 'radiologist'
    lab = 'lab'
    medical_secretary = 'medical_secretary'
    pharmacist = 'pharmacist'
    admin = 'admin'
    user_types = [
        (doctor,'Doctor'),
        (nurse,'Nurse'),
        (patient,'Patient'),
        (receptionist,'Receptionist'),
        (radiologist,'Radiologist'),
        (lab,'Lab'),
        (medical_secretary,'Medical Secretary'),
        (pharmacist,'Pharmacist'),
        (admin,'Admin'),
    ]

    genders = [
        ('M','Male'),
        ('F','Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique= 1)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=1,null=1)
    gender = models.CharField(max_length=1,choices=genders,null=1,blank=1)
    national_id = models.CharField(max_length=14,unique=1,null=1,blank=1)
    birth_date = models.DateField(null=1,blank=1)
    role = models.CharField(max_length=255,choices=user_types,default=patient)

    
  
    
