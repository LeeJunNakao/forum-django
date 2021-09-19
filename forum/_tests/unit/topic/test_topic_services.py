import pytest
from topic.services.topic import create
from topic.models import TITLE_MAX_LENGTH
from _tools.validator.message_error import max_length_message


@pytest.fixture
def valid_data():
    return {"title": "A valid title", "user_id": 1}


@pytest.fixture
def invalid_data():
    return {"title": "A title so big to make it a not valid title", "user_id": "anyone"}


class TestTopicServiceCreate:
    def test_invalid_title(self, invalid_data, topic_model):
        response, status_code = create(**invalid_data, model=topic_model)

        assert status_code == 400
        assert response == {"title": max_length_message(TITLE_MAX_LENGTH)}

    def test_create_topic(self, valid_data, default_user, topic_model):
        response, status_code = create(**valid_data, model=topic_model(default_user))

        assert status_code == 200
        assert response == {
            "title": valid_data["title"],
            "creator": default_user.as_dict(),
        }
