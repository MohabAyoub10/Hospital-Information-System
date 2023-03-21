from django.contrib import admin
from .models import doctor_schedule, slot, booked_appointment

admin.site.register(doctor_schedule)
admin.site.register(slot)
admin.site.register(booked_appointment)
# Register your models here.
