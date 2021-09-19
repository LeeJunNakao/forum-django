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
            "title": "<KLDÇASKDÇLdldaslçdkasçldkaçdksalçdkadçlaksçdlkasçldkao0dopsa0",
            "content": "",
        }

    @pytest.fixture
    def valid_data(self, default_user, default_topic):
        return {
            "title": "Valid Post Title",
            "content": "Some valid text",
            "creator_id": default_user.id,
            "topic_id": default_topic.id,
        }

    def test_create_invalid_data(self, valid_data, invalid_data, post_model):
        response, status = create(
            **{**valid_data, **invalid_data}, post_model=post_model
        )

        assert status == 400
        assert response == {
            "title": max_length_message(TITLE_MAX_LENGTH),
            "content": min_length_message(CONTENT_MIN_LENGTH),
        }

    def test_title_min_length(self, valid_data, post_model):
        title = "".join(["b" for i in range(TITLE_MIN_LENGTH - 1)])
        response, status = create(
            **assoc(valid_data, "title", title), post_model=post_model
        )

        assert status == 400
        assert response == {"title": min_length_message(TITLE_MIN_LENGTH)}

    def test_content_max_length(self, valid_data, post_model):
        content = "".join(["a" for i in range(CONTENT_MAX_LENGTH + 1)])
        response, status = create(
            **assoc(valid_data, "content", content), post_model=post_model
        )

        assert status == 400
        assert response == {"content": max_length_message(CONTENT_MAX_LENGTH)}

    def test_create_valid_data(
        self, valid_data, post_model, default_topic, default_user
    ):
        response, status = create(
            **valid_data,
            post_model=post_model(topic=default_topic, creator=default_user)
        )

        expected_title, expected_content, expected_creator, expected_topic = itemgetter(
            "title", "content", "creator", "topic"
        )(response)
        title, content = itemgetter("title", "content")(response)

        assert status == 200
        assert expected_title == title
        assert expected_content == content
        assert expected_creator == default_user.as_dict()
        assert expected_topic == default_topic.as_dict()
