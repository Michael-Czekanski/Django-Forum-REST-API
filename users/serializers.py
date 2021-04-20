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
