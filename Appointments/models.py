from django.db import models
from Hospital.models import *
from datetime import datetime
# Create your models here.
days = [
    ('Saturday', 'Saturday'), 
    ('Sunday', 'Sunday'), 
    ('Monday', 'Monday'), 
    ('Tuesday', 'Tuesday'), 
    ('Wednesday', 'Wednesday'), 
    ('Thursday', 'Thursday'), 
    ('Friday', 'Friday')
    ]

appointment_status = [('pending', 'pending'), ('completed', 'completed'), ('cancelled', 'cancelled'),('waiting', 'waiting')]
Schedule_Status = [('active', 'active'), ('inactive', 'inactive')]

appointment_duration = [(10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60)]
type_of_appointment = [('new', 'new'), ('followup', 'followup')]

class DoctorSchedule(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_schedule')
    day_of_week = models.CharField(max_length=10, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(choices=appointment_duration)
    schedule_status = models.CharField(max_length=10, choices=Schedule_Status,default='active')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



class Slot(models.Model):

    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE, related_name='slot_schedule')
    start_time = models.TimeField()
    end_time = models.TimeField()


    
    def get_day(self):
        return self.schedule.day_of_week

    



class BookedAppointment(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT,related_name='patient_appointment')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name='doctor_appointment')
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT,related_name='slot_appointment')
    date = models.DateField()
    type = models.CharField(max_length=10, choices=type_of_appointment)
    status = models.CharField(max_length=10, choices=appointment_status)
    created_at = models.DateTimeField(auto_now_add=True)



class DoctorAppointmentsDetails(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name='doctor_appointment_details')
    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.PROTECT,related_name='schedule_appointment_details')
    date = models.DateField()
    total_appointments = models.PositiveIntegerField(default=0)
