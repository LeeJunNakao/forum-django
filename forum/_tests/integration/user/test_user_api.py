import pytest
from toolz import dissoc
from django.urls import reverse

from authentication.models import USERNAME_MIN_LENGTH
from _tools.validator.message_error import (
    min_length_message,
    email_message,
    password_message,
)


class TestUserApiRegister:
    @pytest.fixture
    def valid_data(self):
        return {
            "username": "james",
            "email": "james@email.com",
            "password": "Password152*",
        }

    @pytest.fixture
    def invalid_data(self):
        return {"username": "hh", "email": "notAema.il", "password": "password"}

    @pytest.fixture
    def url(self):
        return reverse("authentication:register")

    @pytest.mark.django_db
    def test_register_user(self, url, valid_data, client):
        response = client.post(
            url,
            data=valid_data,
        )

        assert response.status_code == 200
        assert {**dissoc(valid_data, "password"), "id": 1} == response.json()

    @pytest.mark.django_db
    def test_fail_register_user(self, url, invalid_data, client):
        response = client.post(
            url,
            data=invalid_data,
        )

        assert response.status_code == 400
        assert {
            "username": min_length_message(USERNAME_MIN_LENGTH),
            "email": email_message(),
            "password": password_message(),
        } == response.json()
