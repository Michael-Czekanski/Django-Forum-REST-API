from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from .permissions import IsCreatorOrReadOnly


# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
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


class TopicDetail(APIView):
    permission_classes = [IsCreatorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def __init__(self, *args, **kwargs):
        super(TopicDetail, self).__init__(*args, **kwargs)
        self.topic = None

    def initial(self, request, *args, **kwargs):
        super(TopicDetail, self).initial(request, args, kwargs)
        self.topic = Topic.objects.get(pk=kwargs.get('pk'))
        self.check_object_permissions(request, self.topic)

    def handle_exception(self, exc):
        if isinstance(exc, Topic.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return super(TopicDetail, self).handle_exception(exc)

    def get(self, request, pk):
        serializer = TopicSerializer(self.topic)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = TopicSerializer(instance=self.topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)