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
class doctor_schedule(models.Model):
    
    schedule_id = models.AutoField(primary_key=True)
    # doctor_id = models.IntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    day_of_week = models.CharField(max_length=50, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(choices=appointment_duration)
    schedule_status = models.CharField(max_length=50, choices=Schedule_Status)
    
    def __str__(self):
        return self.schedule_id
    
class slots(models.Model):
    slot_id = models.AutoField(primary_key=True)
    schedule_id = models.ForeignKey(doctor_schedule, on_delete=models.CASCADE)
    slot_start_time = models.TimeField()
    
    slot_end_time = models.TimeField()

    

class booked_appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    appointment_date = models.DateField()
    slot_id = models.ForeignKey(slots, on_delete=models.PROTECT)
    appointment_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=appointment_status)





