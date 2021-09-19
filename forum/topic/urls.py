from django.urls import path

from .views import Topic

app_name = "topic"
urlpatterns = [path("create", Topic.as_view(), name="create")]
