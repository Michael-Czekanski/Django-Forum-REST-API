from rest_framework import serializers
from .models import User
from datetime import datetime


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserDetailSerializer(UserSerializer):
    first_name = serializers.CharField(allow_blank=True, max_length=150)
    last_name = serializers.CharField(allow_blank=True, max_length=150)
    email = serializers.EmailField(allow_blank=True)
    date_joined = serializers.DateTimeField(read_only=True, default=datetime.now())

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
