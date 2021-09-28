import pytest

from topic.models import PostModel, TopicModel

@pytest.fixture
def topic_model(mock_module):
    return mock_module(name="TopicModel", spec=TopicModel)


@pytest.fixture
def post_model(mock_module, mock_function):
    def set_response(expected_response = None):
        model = mock_module(name="PostModel", spec=PostModel)
        model.as_dict.return_value = expected_response
        return mock_function("PostModel Init", model)

    return set_response