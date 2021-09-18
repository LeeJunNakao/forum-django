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
    def __init__(self, title, creator_id):
        self.title = title
        self.creator_id = creator_id
        self._user: UserModel = None

    def as_dict(self):
        return {"title": self.title, "creator": self._user.as_dict()}

    def save(self):
        self.id = 999


@pytest.fixture
def user_model():
    return UserModel


@pytest.fixture
def topic_model():
    def set_user(user):
        def create_topic(title, creator_id):
            topic = TopicModel(title=title, creator_id=creator_id)
            topic._user = user

            return topic

        return create_topic

    return set_user


@pytest.fixture()
def default_user():
    return UserModel(id_=1, name="Mary Gold", email="mary@email.com")
