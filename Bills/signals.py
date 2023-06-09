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
            bill = Bill.objects.create(
                patient=instance.patient, appointment=instance)
            bill.total = instance.slot.schedule.price
            bill.save()


@receiver(post_save, sender=ExamRequest)
def create_radiology_service(sender, instance, **kwargs):
    if instance.status == 'Pending' and instance.type_of_request == 'Radiology':
        bill = Bill.objects.filter(
            patient=instance.patient, appointment=instance.appointment).first()
        if not bill:
            raise Exception(
                'No bill found for the given patient and appointment, becuase the appointment is not booked yet')
        else:
            bill.radiology_request = instance
            for exam in bill.radiology_request.exams.all():
                bill.total += exam.price
            bill.save()


@receiver(post_save, sender=ExamRequest)
def create_lab_service(sender, instance, **kwargs):
    if instance.status == 'Pending' and instance.type_of_request == 'Laboratory':
        bill = Bill.objects.filter(
            patient=instance.patient, appointment=instance.appointment).first()
        if not bill:
            raise Exception(
                'No bill found for the given patient and appointment, becuase the appointment is not booked yet')
        else:
            bill.lab_request = instance
            for exam in bill.lab_request.exams.all():
                bill.total += exam.price
            bill.save()


@receiver(post_save, sender=Prescription)
def create_prescription_service(sender, instance, **kwargs):
    if instance.dispensed_status == 'send_to_pharmacy':
        bill = Bill.objects.filter(
            patient=instance.patient, appointment=instance.appointment).first()
        if not bill:
            raise Exception(
                'No bill found for the given patient and appointment, becuase the appointment is not booked yet')
        else:
            bill.prescription = instance
            for item in instance.prescription.all():
                if item.dispensed == True:
                    bill.total += Decimal(item.drug.price)
            bill.save()


@receiver(post_save, sender=Bill)
def update_bill_total(sender, instance, **kwargs):
    if instance.insurance != None and instance.discount == 0.0:
        coverage_percentage = Decimal(
            str(instance.insurance.coverage_percentage / 100))
        instance.discount = coverage_percentage
        pprint(instance.discount)
        instance.total -= instance.total * coverage_percentage
        instance.save()
