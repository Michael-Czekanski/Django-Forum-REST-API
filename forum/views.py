from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer


# Create your views here.

@api_view(['GET'])
def topics_list(request):
    """
    List of all topics.
    """

    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

