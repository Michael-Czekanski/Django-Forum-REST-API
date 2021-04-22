from django.shortcuts import render
from .models import Topic
from django.http import JsonResponse
from .serializers import TopicSerializer


# Create your views here.

def topics_list(request):
    """
    List of all topics.
    """

    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return JsonResponse(serializer.data, safe=False)

