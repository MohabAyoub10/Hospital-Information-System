from django.contrib import admin
from .models import *



@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'day_of_week', 'start_time', 'end_time', 'slot_duration', 'schedule_status']

# Register your models here.

admin.site.register(Slot)

admin.site.register(BookedAppointment)

admin.site.register(DoctorAppointmentsDetails)
