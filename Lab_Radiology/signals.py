from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from HIS import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender,**kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        if user.role == 'radiologist':
            RadiologyStaff.objects.create(user=user)
        elif user.role == 'lab':
            LabStaff.objects.create(user=user)
          
        
