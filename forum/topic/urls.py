from django.urls import path

from .views import TopicCreate, Post, index, Topic

app_name = "topic"
urlpatterns = [
    path("create", TopicCreate.as_view(), name="create"),
    path("", index, name="index"),
    path("<int:topic_id>", Topic.as_view(), name="topic"),
    path("<int:topic_id>/post", Post.as_view(), name="topic_post"),
]
