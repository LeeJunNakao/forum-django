from authentication.models import User
from topic.models import TopicModel
import pytest


@pytest.fixture
def default_user():
    user = User(username="John Some", email="john@email.com", password="Password52!")
    user.save()

    return user


@pytest.fixture
def default_topic(default_user):
    topic = TopicModel(title="The topic", creator=default_user)
    topic.save()

    return topic
