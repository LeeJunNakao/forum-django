import pytest
from unittest.mock import Mock, MagicMock
from topic.models import PostModel, TopicModel


def set_asdict(name, spec):
    def set(expected_response=None):
        model = Mock(name=name, spec=spec)
        model.as_dict.return_value = expected_response
        return MagicMock(name=f"{name} init", return_value=model)

    return set


@pytest.fixture
def topic_model():
    return set_asdict(name="TopicModel", spec=TopicModel)


@pytest.fixture
def post_model():
    return set_asdict(name="PostModel", spec=PostModel)
