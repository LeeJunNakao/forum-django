from django.urls import path

from .views import Topic, Post, index

app_name = "topic"
urlpatterns = [
    path("create", Topic.as_view(), name="create"),
    path("", index, name="index"),
    path("<int:topic_id>/post", Post.as_view(), name="topic_post"),
]
