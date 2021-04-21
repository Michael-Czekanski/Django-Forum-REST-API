from django.urls import path
from .views import users_list

urlpatterns = [
    path('all/', users_list, name='users_list')
]
