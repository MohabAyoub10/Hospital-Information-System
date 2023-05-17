from rest_framework.permissions import BasePermission, SAFE_METHODS


class ViewOrCreatOrEditExams(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            return request.user.role in ['radiologist','lab','medical_secretary','admin']
        return False


class CanViewOrEdit(BasePermission):
    
    def has_permission(self, request, view):
            if request.user.is_authenticated:
                if request.method in SAFE_METHODS and  request.user.role in ['doctor', 'radiologist','lab','patient','receptionist']:
                    return True
                elif request.method in ['POST','DELETE'] and request.user.role in ['doctor']:
                    return True
                return request.method in ['PATCH','PUT'] and request.user.role in ['doctor', 'radiologist','lab','receptionist']
            return False

    


class CanViewOrEditOrCreatRadiologyResult(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS and request.user.role in ['doctor', 'radiologist','patient']:
                return True
            return request.user.role  == 'radiologist'
        return False

class CanViewOrEditOrCreatLabResult(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS and request.user.role in ['doctor','lab','patient']:
                return True
            return (request.user.role == 'lab')
        return False