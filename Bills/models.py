from django.db import models
from Appointments.models import BookedAppointment
from Hospital.models import Patient
from Lab_Radiology.models import ExamRequest, ExamsList
from django.core.validators import MinValueValidator, MaxValueValidator
from Pharmacy.models import *
        
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]



# Create your models here.

class InsuranceDetails(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='InsuranceDetails')
    company = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    expairy_date = models.DateField()
    coverage = models.TextField()
    coverage_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0.0, validators=PERCENTAGE_VALIDATOR)
    
    card = models.ImageField(upload_to='Bills/files/media')

class Bill(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='Bill')
    time_date = models.DateTimeField(auto_now_add=True)
    insurance = models.ForeignKey(InsuranceDetails, on_delete=models.CASCADE,related_name='Bill', null=True,blank=True)
    appointment = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE,related_name='Bill', null=True,blank=True)
    examrequest = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='Bill', null=True,blank=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE,related_name='Bill', null=True,blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    




