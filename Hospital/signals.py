from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from HIS import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender,**kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        if user.role == 'receptionist':
            Receptionist.objects.create(user=user)
        elif user.role == 'nurse':
            Nurse.objects.create(user=user)
        elif user.role == 'medical_secretary':
            MedicalSecretary.objects.create(user=user)
        elif user.role == 'doctor':
            Doctor.objects.create(user=user)
        elif user.role == 'patient':
            Patient.objects.create(user=user)
        
