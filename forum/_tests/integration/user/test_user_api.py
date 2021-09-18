import pytest
from django.urls import reverse
from authentication.models import NAME_MIN_LENGTH
from _tools.validator.message_error import min_length_message, email_message


class TestUserApiRegister:
    @pytest.fixture
    def valid_data(self):
        return {"name": "James", "email": "james@email.com"}

    @pytest.fixture
    def invalid_data(self):
        return {"name": "hh", "email": "notAema.il"}

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
        assert {**valid_data, "id": 1} == response.json()

    @pytest.mark.django_db
    def test_fail_register_user(self, url, invalid_data, client):
        response = client.post(
            url,
            data=invalid_data,
        )

        assert response.status_code == 400
        assert {
            "name": min_length_message(NAME_MIN_LENGTH),
            "email": email_message(),
        } == response.json()
