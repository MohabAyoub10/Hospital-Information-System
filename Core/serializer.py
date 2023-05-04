from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','phone_1','phone_2','gender','national_id'] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','phone_1','phone_2','email','gender','national_id','birth_date','role']
        read_only_fields = ['username','role']
    
