from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer


# Create your views here.

def users_list(request):
    """
    List all users.
    """

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
