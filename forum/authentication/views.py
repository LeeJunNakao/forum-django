from operator import itemgetter
from django.http import HttpResponse
from django.template import loader
from django.views import View
from authentication.services import auth as service
from _tools.parser.http import json_resp
from authentication.models import User


class Register(View):
    def get(self, request):
        template = loader.get_template("register.html")

        return HttpResponse(template.render(request=request))

    def post(self, request):
        username, email, password = itemgetter("username", "email", "password")(
            request.POST
        )
        response, status = service.register(username, email, password, User)

        return json_resp(response, status)


class Login(View):
    def get(self, request):
        template = loader.get_template("login.html")

        return HttpResponse(template.render(request=request))

    def post(self, request):
        username, password = itemgetter('username', 'password')(request.POST)
        response, status = service.login(request, username=username, password=password)

        return json_resp(response, status)
