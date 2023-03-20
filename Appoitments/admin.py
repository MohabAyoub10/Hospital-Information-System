from django.contrib import admin
from .models import doctor_schedule, slots, booked_appointment

admin.site.register(doctor_schedule)
admin.site.register(slots)
admin.site.register(booked_appointment)
# Register your models here.
