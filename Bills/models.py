from django.db import models
from Appointments.models import BookedAppointment
from Hospital.models import Patient
from Lab_Radiology.models import ExamRequest



# Create your models here.

class InsuranceDetails(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='InsuranceDetails')
    company = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    expairy_date = models.DateField()
    coverage = models.TextField()
    card = models.ImageField(upload_to='Bills/files/media')

class Bill(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='Bill')
    time_date = models.DateTimeField(auto_now_add=True)
    insurance = models.ForeignKey(InsuranceDetails, on_delete=models.CASCADE,related_name='Bill', null=True,blank=True)
    


class AppointmentService(models.Model):

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='AppointmentService')
    appointment = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE,related_name='AppointmentService')

class ExamService(models.Model):

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='ExamService')
    exam_request = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='ExamService')



class MedicineService(models.Model):

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='MedicineService')
    #medication = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE,related_name='MedicineService')




