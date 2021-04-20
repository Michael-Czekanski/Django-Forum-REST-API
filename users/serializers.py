from rest_framework import serializers
from .models import User
from datetime import datetime

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(allow_blank=True, max_length=150)
    last_name = serializers.CharField(allow_blank=True, max_length=150)
    email = serializers.EmailField(allow_blank=True)
    password = serializers.CharField()
    date_joined = serializers.DateTimeField(default=datetime.now())

    def create(self, validated_data):
        """
        Create and return a new 'User' instance, given the validated data.
        """

        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
