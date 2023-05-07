from rest_framework.permissions import BasePermission

class IsPharmacistOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'pharmacist' or request.method in ['GET', 'HEAD', 'OPTIONS']


class IsAdminOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return  request.user.role == 'admin' or request.method in ['GET', 'HEAD', 'OPTIONS']


class IsDoctorOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return  request.user.role == 'doctor' or request.method in ['GET', 'HEAD', 'OPTIONS']

class IsReceptionistOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return  request.user.role == 'receptionist' or request.method in ['GET', 'HEAD', 'OPTIONS']