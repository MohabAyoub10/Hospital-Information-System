from django.db import models
from datetime import datetime
from django.conf import settings
from Hospital.models import Patient, Doctor
from Appointments.models import BookedAppointment


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
    appointment = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE, related_name='appointment_exam')
    status = models.CharField(max_length=10, choices=STATUS, default=REQUESTED)
    dateTime = models.DateTimeField(default=datetime.now)


class RadiolgyResult(models.Model):
    Request = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='radiolgy_request')
    dateTime = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='Lab_Radiology/files/media')
    report_file = models.FileField(upload_to='Lab_Radiology/files')
    comment = models.TextField(blank=True)


class TestResult(models.Model):
    Request = models.ForeignKey(ExamRequest, on_delete=models.CASCADE, related_name='test_request')
    dateTime = models.DateTimeField(default=datetime.now)
    result_value = models.DecimalField( max_digits=10, decimal_places=5)
    unit = models.CharField(max_length=50)
    min_reference_range = models.DecimalField(max_digits=10, decimal_places=5)
    max_reference_range = models.DecimalField(max_digits=10, decimal_places=5)
    comment = models.TextField(blank=True)


class ExaminationList(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.exam_name


class ExamDetails(models.Model):
    exam = models.ForeignKey(ExaminationList, null=False, on_delete=models.PROTECT, related_name='exam')
    request = models.ForeignKey(ExamRequest, null=False, on_delete=models.CASCADE, related_name='request')



class LabRadiologyStaff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
