from operator import itemgetter
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.db import transaction
from django.shortcuts import render
from topic.services.topic import create as create_topic
from topic.services.post import create as create_post
from _tools.parser.http import json_resp
from topic.models import TopicModel, PostModel


class Topic(View):
    def get(self, request):
        template = loader.get_template("topic.html")
        return HttpResponse(template.render(request=request))

    def post(self, request):
        title, user_id = itemgetter("title", "user_id")(request.POST)

        with transaction.atomic():
            response, status = create_topic(title, user_id, TopicModel)

        return json_resp(response, status)


class Post(View):
    def get(self, request, topic_id):
        return render(request, "post.html", {"topic_id": topic_id})

    def post(self, request, topic_id):
        title, content, user_id = itemgetter("title", "content", "creator_id")(
            request.POST
        )

        response, status = create_post(
            title=title,
            content=content,
            creator_id=user_id,
            topic_id=topic_id,
            topic_model=TopicModel,
            post_model=PostModel,
        )

        return json_resp(response, status)
