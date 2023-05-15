from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from Lab_Radiology.models import *
from Pharmacy.models import *
from pprint import pprint 


@receiver(post_save, sender=ExamRequest)
def create_exam_service(sender, instance, **kwargs):
    if instance.status == 'Pending':
        bill = Bill.objects.filter(patient=instance.patient, appointment=instance.appointment).first()
        bill.examrequest = instance
        for exam in instance.exams.all():
            bill.total += exam.price
        bill.save()


# @receiver(post_save, sender=Prescription)
# def create_prescription_service(sender, instance, **kwargs):
#     if instance.dispensed_confirm == True:
#         bill = Bill.objects.filter(patient=instance.patient, appointment=instance.appointment).first()
#         bill.prescription = instance
#         for item in instance.prescription.all():
#             pprint(item.drug.price)
#             bill.total += item.drug.price
#         bill.save()