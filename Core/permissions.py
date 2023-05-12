from rest_framework.permissions import BasePermission
from Core.utils import permission_exception_handler

class IsAdminOrReceptionist(BasePermission):
    def has_permission(self, request, view):
        return  permission_exception_handler(request, 'receptionist') or permission_exception_handler(request, 'admin') 

