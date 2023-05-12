from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .permissions import *

class UserViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReceptionist]
    def get_queryset(self):
        if self.request.user.role == 'receptionist':
            return User.objects.filter(role='patient').all()
        return  User.objects.all()
    def get_serializer_class(self):
        if self.request.user.role == 'admin' or self.request.method == 'GET':
            return AdminUserCreateSerializer
        return UserCreateSerializer