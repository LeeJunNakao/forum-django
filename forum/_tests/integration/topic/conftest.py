from authentication.models import User
import pytest


@pytest.fixture
def default_user():
    user = User(name="John Some", email="john@email.com")
    user.save()

    return user
