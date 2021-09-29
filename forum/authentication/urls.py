from django.urls import path

from .views import Register, Login

app_name = "authentication"
urlpatterns = [
    path("register", Register.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
]
