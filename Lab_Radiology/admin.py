from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ExamsList)
class ExaminationListAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price']




admin.site.register(ExamRequest)
admin.site.register(TestResult)
admin.site.register(RadiologyResult)
admin.site.register(RadiologyResultDetails)




