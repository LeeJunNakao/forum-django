import pytest
from authentication.models import User


@pytest.fixture()
def mock_function(mocker):
    return lambda name, return_value: mocker.MagicMock(
        name=name, return_value=return_value
    )


@pytest.fixture()
def mock_module(mocker):
    return lambda name, spec: mocker.Mock(name=name, spec=spec)


@pytest.fixture
def default_user():
    return {
        "id": 1,
        "username": "Mary Gold",
        "email": "mary@email.com",
        "password": "Password526@",
    }


@pytest.fixture
def default_topic(topic_model, default_user):
    return {"title": "Valid Topic Title", "creator_id": default_user.get("id")}
