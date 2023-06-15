from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from HIS import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, **kwargs):

    if kwargs['created']:
        user = kwargs['instance']
        if user.role == 'pharmacist':
            Pharmacist.objects.create(user=user)


@receiver(post_save, sender=Prescription)
def update_drug_stock(sender, instance, **kwargs):
    if instance.dispensed_status == 'dispensed':
        for item in instance.prescription.all():
            if item.dispensed == True:
                drug = item.drug
                drug.stock -= item.amount
                drug.save()
