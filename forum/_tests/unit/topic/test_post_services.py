from unittest.mock import MagicMock
import pytest
from operator import itemgetter
from toolz import assoc
from topic.services.post import create
from _tools.validator.message_error import max_length_message, min_length_message
from topic.models import (
    TITLE_MAX_LENGTH,
    TITLE_MIN_LENGTH,
    CONTENT_MIN_LENGTH,
    CONTENT_MAX_LENGTH,
)


class TestPostServiceCreate:
    @pytest.fixture
    def invalid_data(self):
        return {
            "content": "",
        }

    @pytest.fixture
    def valid_data(self, default_user, default_topic):
        return {
            "content": "Some valid text",
            "creator_id": default_user.get("id"),
            "topic_id": default_topic.get("id"),
        }

    def test_create_invalid_data(
        self, valid_data, invalid_data, topic_model, post_model
    ):
        response, status = create(
            **{**valid_data, **invalid_data},
            topic_model=topic_model(),
            post_model=post_model(),
        )

        assert status == 400
        assert response == {
            "content": min_length_message(CONTENT_MIN_LENGTH),
        }

    def test_content_max_length(self, valid_data, topic_model, post_model):
        content = "".join(["a" for i in range(CONTENT_MAX_LENGTH + 1)])
        response, status = create(
            **assoc(valid_data, "content", content),
            topic_model=topic_model,
            post_model=post_model(),
        )

        assert status == 400
        assert response == {"content": max_length_message(CONTENT_MAX_LENGTH)}

    def test_create_valid_data(
        self,
        valid_data,
        topic_model,
        post_model,
        default_topic,
        default_user,
    ):
        expected_response = {
            "content": valid_data.get("content"),
            "creator": default_user,
            "topic": default_topic,
        }

        response, status = create(
            **valid_data,
            topic_model=topic_model(valid_data)(),
            post_model=post_model(expected_response),
        )

        expected_content, expected_creator, expected_topic = itemgetter(
            "content", "creator", "topic"
        )(response)
        content = itemgetter("content")(response)

        assert status == 200
        assert expected_content == content
        assert expected_creator == default_user
        assert expected_topic == default_topic
