from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreateOrEditOrDeleteInsuranceDetails(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist', 'patient']
    


class BillPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role in ['receptionist', 'patient']
        else :
            return request.user.is_authenticated and request.user.role == 'receptionist'
