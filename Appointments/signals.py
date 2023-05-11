from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from  datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from pprint import pprint
from django.template.loader import render_to_string
from .templates import *


def converter(time):
    hours = int(time[0] + time[1])
    minutes = int(time[3] + time[4])
    new_time = timedelta(minutes=minutes,hours=hours)
    return new_time

@receiver(post_save, sender=DoctorSchedule)
def create_slots(sender, instance,created, **kwargs):
    if created:
        i = instance
        start = converter(str(i.start_time))
        end = start
        while start < converter(str(i.end_time)):
            end = start + timedelta(minutes=i.slot_duration) 
            Slot.objects.create(schedule_id=i.pk, start_time=str(start), end_time=str(end))
            start = end


@receiver(post_delete, sender=DoctorSchedule)
def delete_slots(sender, instance, **kwargs):
    Slot.objects.filter(schedule_id=instance.pk).delete()



from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BookedAppointment, DoctorAppointmentsDetails

@receiver(post_save, sender=BookedAppointment)
def create_appointments_records(sender, instance, created, **kwargs):
    if created:
        details, created = DoctorAppointmentsDetails.objects.get_or_create(doctor=instance.doctor, date=instance.date, schedule=instance.slot.schedule)
        details.total_appointments += 1
        details.save()

@receiver(post_delete, sender=DoctorAppointmentsDetails)
def cancel_all_booked_appointments(sender, instance, **kwargs):
    booking = BookedAppointment.objects.filter(doctor=instance.doctor, date=instance.date)
    pprint(booking[0].patient.user.email)
    booking.delete()
    send_cansellation_email('mohab.ayoub10@gmail.com')



def send_cansellation_email(email):
    render_temp = render_to_string('mail.html', {'Patient': 'Mohabb'})
    send_mail("Appointment Cansellation", '','hishospital521@gmail.com',['mo.ayoub411@gmail.com'],html_message=render_temp)
