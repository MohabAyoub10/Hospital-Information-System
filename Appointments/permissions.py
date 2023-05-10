from rest_framework.permissions import BasePermission, SAFE_METHODS


def is_admin_or_staff(user):
    return user.is_authenticated and user.role in ['admin', 'receptionist', 'doctor']


class CanAccess(BasePermission):

    def has_permission(self, request, view):
        return is_admin_or_staff(request.user) and request.user.role == 'patient'


class CreateDoctorScheduleOrUpdate(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and is_admin_or_staff(request.user):
            return True
        elif request.method in SAFE_METHODS and request.user.role == 'patient' and request.user.is_authenticated:
            return True
        return is_admin_or_staff(request.user) and request.user.role == 'receptionist'


class BookAppointment(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS and is_admin_or_staff(request.user):
                 return True
            return request.user.role in ['patient', 'receptionist']
        return False