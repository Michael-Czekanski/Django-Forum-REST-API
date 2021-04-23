from rest_framework import status
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(APIView):

    def get(self, request):
        """
        Return list of all users.
        """

        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


class UserDetail(APIView):

    def get(self, request, pk):
        """
        Return details of user.
        """

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
