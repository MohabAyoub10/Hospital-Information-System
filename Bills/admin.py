from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(InsuranceDetails)
admin.site.register(Bill)
admin.site.register(ExamService)
admin.site.register(MedicineService)
admin.site.register(AppointmentService)


