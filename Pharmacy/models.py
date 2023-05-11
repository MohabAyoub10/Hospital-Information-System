from django.db import models
from django.conf import settings
from Hospital.models import Patient,Doctor
# from Appointments.models import BookedAppointment
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Prescription(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='doctor')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient')
    # appointment = models.ForeignKey(BookedAppointment,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    dispensed_by = models.ForeignKey('Pharmacist',on_delete=models.CASCADE, null=True, blank=True, related_name='dispensed_by')
    dispensed_confirm = models.BooleanField(default=False)


class Drug(BaseModel):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    expire_date = models.DateField()
    form = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

class Pharmacist(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='pharmacist')
    license = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
class PrescriptionItems(BaseModel):
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name='prescription')
    drug = models.ForeignKey(Drug,on_delete=models.CASCADE, related_name='drug')
    dose = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    amount = models.IntegerField()
    dispensed = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.drug} - {self.dose} - {self.duration}'
