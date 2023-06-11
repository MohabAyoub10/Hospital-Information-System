from rest_framework.permissions import BasePermission, SAFE_METHODS


def is_admin_or_staff(user):
    return user.is_authenticated and user.role in ['admin', 'receptionist', 'doctor']


def is_receptionist(user):
    return user.is_authenticated and user.role == 'receptionist'


def is_patient(user):
    return user.is_authenticated and user.role == 'patient'


def is_doctor(user):
    return user.is_authenticated and user.role == 'doctor'


class CanAccess(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS and request.user.role in ['patient', 'receptionist', 'doctor']:
                return True
            else:
                return False
        return False


class CreateDoctorScheduleOrUpdate(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and is_admin_or_staff(request.user):
            return True
        elif request.method in SAFE_METHODS and request.user.role == 'patient' and request.user.is_authenticated:
            return True
        elif request.method in ['POST', 'PUT', 'PATCH'] and is_receptionist(request.user):
            return True
        return False


class BookAppointment(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS and is_admin_or_staff(request.user):
                return True
            return request.user.role in ['patient', 'receptionist']
        return False


class DoctorAppointmentPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method:
            return request.user.role in ['doctor', 'receptionist']
