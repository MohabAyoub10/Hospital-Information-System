from django.contrib import admin
from .models import *
from . import models
# Register your models here.
@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['__str__','specialty','mediaAdmin']

admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Address)
admin.site.register(Specialty)
admin.site.register(Department)