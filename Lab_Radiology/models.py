from django.db import models
from datetime import datetime
from django.conf import settings
from Hospital.models import Patient, Doctor
from Appointments.models import BookedAppointment

class ExamsList(models.Model):
    Examtypes = [
        ('Radiology', 'Radiology'),
        ('Laboratory', 'Laboratory'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=Examtypes)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class ExamRequest(models.Model):
    REQUESTED = 'Requested'
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS = [
        (REQUESTED, 'Requested'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]
    exams = models.ManyToManyField(ExamsList)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_exame')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_exame')
    appointment = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE, related_name='appointment_exame')
    status = models.CharField(max_length=255, choices=STATUS, default=REQUESTED)
    dateTime = models.DateTimeField(default=datetime.now)
    comment = models.TextField(blank=True)



class RadiologyResult(models.Model):
    Request = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='radiolgy_request')
    exam = models.ForeignKey(ExamsList, on_delete=models.CASCADE, related_name='radiology_exam')
    dateTime = models.DateTimeField(default=datetime.now)
    report_file = models.FileField(upload_to='Lab_Radiology/files')
    

class RadiologyResultDetails(models.Model):
    result = models.ForeignKey(RadiologyResult, on_delete=models.CASCADE, related_name='radiology_result')
    image = models.ImageField(upload_to='Lab_Radiology/files/media')
    comment = models.TextField(blank=True)


class TestResult(models.Model):
    Request = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='Lab_request')
    exam = models.ForeignKey(ExamsList, on_delete=models.CASCADE, related_name='Lab_exam')
    dateTime = models.DateTimeField(default=datetime.now)
    pdf_result = models.FileField(upload_to='Lab_Radiology/files')
    comment = models.TextField(blank=True)


class LabRadiologyStaff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
