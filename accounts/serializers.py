from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    # email = serializers.EmailField()
    # password = serializers.CharField()
    # token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    # def get_token(self, username):
    #     """Token generation method"""
    #     user = get_user_model().objects.get(username=username)
    #     return Token.objects.get_or_create(user=user)

    # def create(self, validated_data):
    #     user = get_user_model().objects.create_user(**validated_data)
    #     token = Token.objects.create(user=user)
    #     user.token = token.key
    #     return user

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(write_only=True)
    # token = serializers.CharField(min_length=7, max_length=100, read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)
        if user is None:
            raise serializers.ValidationError({"detail": "Invalid Credentials"})
        # token, created = Token.objects.get_or_create(user=user)
        return data
        