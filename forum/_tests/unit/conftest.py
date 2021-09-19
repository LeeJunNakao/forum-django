from typing import Type
from toolz import curry
import pytest


class UserModel:
    def __init__(self, name, email, id_=None):
        self.id = id_
        self.name = name
        self.email = email

    def as_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    def save(self):
        self.id = 999


class TopicModel:
    def __init__(self, title, creator_id, id_=None):
        self.title = title
        self.creator_id = creator_id
        self._user: UserModel = None
        self.id = id_

    def as_dict(self):
        return {"title": self.title, "creator": self._user.as_dict()}

    def save(self):
        self.id = 888


class PostModel:
    def __init__(
        self,
        title,
        content,
        topic_id,
        creator_id,
        creator: Type[UserModel],
        topic: Type[TopicModel],
        id_=None,
    ):
        self.title = title
        self.content = content
        self.topic_id = topic_id
        self.creator_id = creator_id
        self.id = id_
        self._creator = creator
        self._topic = topic

    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "creator": self._creator.as_dict(),
            "topic": self._topic.as_dict(),
            "id": self.id,
        }

    def save(self):
        self.id = 777


@pytest.fixture
def user_model():
    return UserModel


@pytest.fixture
def topic_model():
    def set_user(user):
        def create_topic(title, creator_id, id_=None):
            topic = TopicModel(title=title, creator_id=creator_id, id_=id_)
            topic._user = user

            return topic

        return create_topic

    return set_user


@pytest.fixture
def post_model():
    @curry
    def set_post(title, content, topic_id, creator_id, creator, topic, id_=None):
        return PostModel(
            title=title,
            content=content,
            topic_id=topic_id,
            creator_id=creator_id,
            creator=creator,
            topic=topic,
            id_=id_,
        )

    return set_post


@pytest.fixture
def default_user():
    return UserModel(id_=1, name="Mary Gold", email="mary@email.com")


@pytest.fixture
def default_topic(topic_model, default_user):
    return topic_model(default_user)(
        title="Valid Topic Title", creator_id=default_user.id
    )
