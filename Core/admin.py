from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
   add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","first_name","last_name","email","gender","phone","national_id","birth_date"),
            },
        ),
    )
