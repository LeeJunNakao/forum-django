from authentication.models import User
from topic.models import TopicModel
from django.test import Client
import pytest


@pytest.fixture
def default_user_data():
    return {
        "username": "John Some",
        "email": "john@email.com",
        "password": "Password52!",
    }


@pytest.fixture
def default_user(default_user_data):
    user = User.objects.create_user(**default_user_data)
    user.save()

    return user


@pytest.fixture
def logged_client(default_user_data):
    client = Client()
    client.login(**default_user_data)

    return client


@pytest.fixture
def default_topic(default_user):
    topic = TopicModel(
        title="The topic", content="The topic description", creator=default_user
    )
    topic.save()

    return topic
