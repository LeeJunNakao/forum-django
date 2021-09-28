from operator import itemgetter
import pytest
from toolz import assoc
from django.urls import reverse
from _tools.validator.message_error import max_length_message
from topic.models import TITLE_MAX_LENGTH


class TestTopicApiCreate:
    @pytest.fixture
    def valid_data(self):
        return {"title": "A valid title", "content": "A valid topic content.", "user_id": 1}

    @pytest.fixture
    def invalid_data(self):
        return {"title": "A title so big to make it a not valid title"}

    @pytest.fixture
    def url(self):
        return reverse("topic:create")

    @pytest.mark.django_db
    def test_create_topic(self, url, valid_data, default_user, logged_client):
        response = logged_client.post(url, data=valid_data)
        title, creator, content = itemgetter(
            "title", "creator", "content")(response.json())

        assert response.status_code == 200
        assert title == valid_data.get("title")
        assert creator == default_user.as_dict()
        assert content == valid_data.get("content")

    @pytest.mark.django_db
    def test_create_invalid_topic(self, url, valid_data, default_user, invalid_data, logged_client):
        response = logged_client.post(url, data={**valid_data, **invalid_data})

        assert response.status_code == 400
        assert response.json() == {"title": max_length_message(TITLE_MAX_LENGTH)}
