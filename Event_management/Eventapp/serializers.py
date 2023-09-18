from rest_framework import serializers
from .models import UserLogin,UserRegister

class LoginuserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLogin
        fields='__all__'

class RegisteruserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields='__all__'

