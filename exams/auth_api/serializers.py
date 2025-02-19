from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from auth_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """Проверка длины пароля"""
        if len(value) < 8:
            raise serializers.ValidationError("Error: Password must be at least 8 characters long")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Хэшируем пароль
        return super().create(validated_data)
