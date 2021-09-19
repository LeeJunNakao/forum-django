from operator import itemgetter
from django.http import HttpResponse
from django.template import loader
from django.views import View
from topic import services
from _tools.parser.http import json_resp
from topic.models import TopicModel
from django.db import transaction


class Topic(View):
    def get(self, request):
        template = loader.get_template("topic.html")
        return HttpResponse(template.render(request=request))

    def post(self, request):
        title, user_id = itemgetter("title", "user_id")(request.POST)

        with transaction.atomic():
            response, status = services.create(title, user_id, TopicModel)

        return json_resp(response, status)
