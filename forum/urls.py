from django.urls import path
from .views import topics_list, TopicDetail

urlpatterns = [
    path('topics/', topics_list, name='forum-topics'),
    path('topics/<int:pk>/', TopicDetail.as_view(), name='forum-topic-detail')
]
