from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from djoser.views import UserViewSet as BaseUserViewSet
from djoser.conf import settings
# Create your views here.
class UserViewSet(BaseUserViewSet):
    http_method_names = ('post','put')
    def get_serializer_class(self):
        if self.request.user.is_staff and self.action == 'create':
            return AdminUserCreateSerializer
        elif self.request.user.role == 'receptionist' and self.action == 'create':
            return UserCreateSerializer
        return settings.SERIALIZERS.user