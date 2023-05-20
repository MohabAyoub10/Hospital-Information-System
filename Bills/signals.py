from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from Lab_Radiology.models import *
from Pharmacy.models import *
from pprint import pprint 
from decimal import Decimal


@receiver(post_save, sender=BookedAppointment)
def create_bill_service(sender, instance, **kwargs):
    if instance.status == 'waiting':
        if not Bill.objects.filter(patient=instance.patient, appointment=instance).exists():
            bill = Bill.objects.create(patient=instance.patient, appointment=instance)
            bill.total = instance.slot.schedule.price
            bill.save()



@receiver(post_save, sender=ExamRequest)
def create_exam_service(sender, instance, **kwargs):
    if instance.status == 'Pending':
        bill = Bill.objects.filter(patient=instance.patient, appointment=instance.appointment).first()
        if not bill:
            raise Exception('No bill found for the given patient and appointment, becuase the appointment is not booked yet')
        bill.examrequest = instance
        for exam in instance.exams.all():
            bill.total += exam.price
        bill.save()


@receiver(post_save, sender=Prescription)
def create_prescription_service(sender, instance, **kwargs):
    if instance.dispensed_status == 'send_to_pharmacy':
        bill = Bill.objects.filter(patient=instance.patient, appointment=instance.appointment).first()
        bill.prescription = instance
        for item in instance.prescription.all():
            bill.total += Decimal(item.drug.price)
        bill.save()
