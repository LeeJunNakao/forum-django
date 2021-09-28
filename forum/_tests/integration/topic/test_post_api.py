from operator import itemgetter
import pytest
from toolz import dissoc
from django.urls import reverse
from _tools.validator.message_error import min_length_message
from topic.models import TITLE_MIN_LENGTH, CONTENT_MIN_LENGTH


class TestPostApiCreate:
    @pytest.fixture
    def url(self):
        def get_url(topic_id):
            return reverse("topic:topic_post", kwargs={"topic_id": topic_id})

        return get_url

    @pytest.fixture
    def invalid_data(self):
        return {"title": "", "content": ""}

    @pytest.fixture
    def valid_data(self, default_user, default_topic):
        return {
            "title": "Some title",
            "content": "The post content text.",
            "topic_id": default_topic.id,
            "creator_id": default_user.id,
        }

    @pytest.mark.django_db
    def test_create_post(self, url, valid_data, client):
        topic_id = valid_data.get("topic_id")
        url_path = url(topic_id)
        response = client.post(url_path, data=dissoc(valid_data, "topic_id"))

        title, content, creator, topic = itemgetter(
            "title", "content", "creator", "topic"
        )(response.json())
        expected_title, expected_content = itemgetter("title", "content")(valid_data)

        assert response.status_code == 200
        assert (title, content) == (expected_title, expected_content)
        assert creator.get("id") == valid_data.get("creator_id")

    @pytest.mark.django_db
    def test_create_invalid_data(self, url, invalid_data, valid_data, client):
        topic_id = valid_data.get("topic_id")
        url_path = url(topic_id)
        response = client.post(url_path, data={**valid_data, **invalid_data})

        assert response.status_code == 400
        assert response.json() == {
            "content": min_length_message(CONTENT_MIN_LENGTH),
            "title": min_length_message(TITLE_MIN_LENGTH),
        }

    @pytest.mark.django_db
    def test_create_invalid_topic_id(self, url, valid_data, client):
        url_path = url(777)
        response = client.post(url_path, data={**valid_data})

        assert response.status_code == 400
        assert response.json() == {"error": "Could not create topic"}
