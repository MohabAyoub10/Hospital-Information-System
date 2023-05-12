from .models import BookedAppointment, DoctorAppointmentsDetails, DoctorSchedule, Slot
from django.db.models.signals import post_save, post_delete
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.dispatch import receiver
from datetime import timedelta



# to convert time from string to timedelta
def converter(time):
    hours = int(time[0:2])
    minutes = int(time[3:5])
    return timedelta(minutes=minutes, hours=hours)

# to create slots when a schedule is created
@receiver(post_save, sender=DoctorSchedule)
def create_slots(sender, instance, created, **kwargs):
    if created:
        start = converter(str(instance.start_time))
        end = start
        while start < converter(str(instance.end_time)):
            end = start + timedelta(minutes=instance.slot_duration)
            Slot.objects.create(schedule=instance, start_time=str(start), end_time=str(end))
            start = end

# delete slots when a schedule is deleted
@receiver(post_delete, sender=DoctorSchedule)
def delete_slots(sender, instance, **kwargs):
    Slot.objects.filter(schedule=instance).delete()

# to create a record for a doctor when a booked appointment is created
@receiver(post_save, sender=BookedAppointment)
def create_appointments_records(sender, instance, created, **kwargs):
    if created:
        details, created = DoctorAppointmentsDetails.objects.get_or_create(
            doctor=instance.doctor, date=instance.date, schedule=instance.slot.schedule
        )
        details.total_appointments += 1
        details.save()

# delete a record for a doctor when a booked appointment is deleted and send a cancellation email
@receiver(post_delete, sender=DoctorAppointmentsDetails)
def cancel_all_booked_appointments(sender, instance, **kwargs):
    bookings = BookedAppointment.objects.filter(doctor=instance.doctor, date=instance.date)
    for appointment in bookings:
        name = appointment.patient.user.first_name + ' ' + appointment.patient.user.last_name
        send_cancellation_email(appointment.patient.user.email, name, appointment.date, appointment.slot.start_time)
    bookings.delete()

# send a cancellation email
def send_cancellation_email(email, name, date, time):
    render_temp = render_to_string('mail.html', {'Patient': name, 'date': date, 'time': time})
    send_mail("Appointment Cancellation",'','hishospital521@gmail.com',[email],html_message=render_temp)