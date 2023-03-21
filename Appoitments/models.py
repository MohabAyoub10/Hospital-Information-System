from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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

appointment_status = [('pend', 'pending'), ('comp', 'completed'), ('canc', 'cancelled')]
Schedule_Status = [('active', 'active'), ('inactive', 'inactive')]

appointment_duration = [(5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60)]
type_of_appointment = [('new', 'new'), ('followup', 'followup')]

class doctor_schedule(models.Model):
    
    schedule_id = models.AutoField(primary_key=True)
    # doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(choices=appointment_duration)
    schedule_status = models.CharField(max_length=50, choices=Schedule_Status)





class slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    schedule_id = models.ForeignKey(doctor_schedule, on_delete=models.CASCADE)
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()

    



class booked_appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    # doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    # patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    slot_id = models.ForeignKey(slot, on_delete=models.PROTECT)
    appointment_type = models.CharField(max_length=50, choices=type_of_appointment)
    status = models.CharField(max_length=50, choices=appointment_status)





