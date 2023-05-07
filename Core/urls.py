from django.urls import path
from Core.views import *
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework.routers import DefaultRouter
from .views import*

router = DefaultRouter()
router.register('auth/register',UserViewSet,basename='register')

urlpatterns = [
    path ('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
urlpatterns += router.urls