from django.urls import path
from .views import topics_list, topic_detail

urlpatterns = [
    path('topics/', topics_list, name='forum-topics'),
    path('topics/<int:pk>/', topic_detail, name='forum-topic-detail')
]
