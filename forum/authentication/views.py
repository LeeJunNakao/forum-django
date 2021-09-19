from operator import itemgetter
from django.http import HttpResponse
from django.template import loader
from django.views import View
from authentication.services import auth as service
from _tools.parser.http import json_resp
from authentication.models import User


class Register(View):
    def get(self, request):
        template = loader.get_template("topic.html")
        return HttpResponse(template.render(request=request))

    def post(self, request):

        name, email = itemgetter("name", "email")(request.POST)
        response, status = service.register(name, email, User)
        return json_resp(response, status)
