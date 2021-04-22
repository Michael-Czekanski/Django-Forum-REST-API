from rest_framework import serializers
from django.utils import timezone
from .models import Topic
from users.models import User


class TopicSerializer(serializers.Serializer):
    # read_only, because it shouldn't be updated or used to create during deserialization
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    # read_only, because it shouldn't be updated or used to create during deserialization
    creation_date = serializers.DateTimeField(read_only=True, default=timezone.now)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
