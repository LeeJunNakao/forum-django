from operator import itemgetter
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.db import transaction
from django.shortcuts import render
from topic.services.topic import create as create_topic, get as get_topic
from topic.services.post import create as create_post
from topic.services.forum import get_all_topics
from _tools.parser.http import json_resp
from topic.models import TopicModel, PostModel
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    topics, _ = get_all_topics(TopicModel)
    return render(request, "home.html", {"topics": topics})


class TopicCreate(LoginRequiredMixin, View):
    login_url = "/api/auth/login"

    def get(self, request):
        template = loader.get_template("topic_create.html")
        return HttpResponse(template.render(request=request))

    def post(self, request):
        title, user_id, content = itemgetter("title", "user_id", "content")(
            request.POST
        )

        response, status = create_topic(title, user_id, content, TopicModel)

        return json_resp(response, status)


class Topic(LoginRequiredMixin, View):
    login_url = "/api/auth/login"

    def get(self, request, topic_id):
        topic, _ = get_topic(topic_id, TopicModel)

        return render(request, "topic.html", {"topic": topic})


class Post(LoginRequiredMixin, View):
    login_url = "/api/auth/login"

    def get(self, request, topic_id):
        return render(request, "post.html", {"topic_id": topic_id})

    def post(self, request, topic_id):
        content, user_id = itemgetter("content", "creator_id")(
            request.POST
        )

        response, status = create_post(
            content=content,
            creator_id=user_id,
            topic_id=topic_id,
            topic_model=TopicModel,
            post_model=PostModel,
        )

        return json_resp(response, status)
