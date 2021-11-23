from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=4, write_only=True)
    email = serializers.EmailField(max_length=100, min_length=5)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Email': 'Email already Exist'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']