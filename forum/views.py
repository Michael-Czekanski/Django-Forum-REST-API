from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def topics_list(request):
    """
    List of all topics or create topic.
    """

    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
