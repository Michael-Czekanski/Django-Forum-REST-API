from django.urls import path
from .views import topics_list

urlpatterns = [
    path('topics/', topics_list, name='forum-topics')
]
