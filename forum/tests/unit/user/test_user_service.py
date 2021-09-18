import pytest
from authentication.services.auth import (
    register,
    NAME_MAX_LENGTH,
    NAME_MIN_LENGTH,
    EMAIL_MAX_LENGTH,
)
from _tools.validator.message_error import (
    max_length_message,
    min_length_message,
    email_message,
)


class UserModel:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def save(self):
        self.id = 999

    def as_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class TestUserServiceRegister:
    @pytest.fixture
    def valid_data(self):
        return {"name": "Valid Name", "email": "valid_email@email.com"}

    @pytest.fixture
    def invalid_data(self):
        return {
            "name": "sd",
            "email": "ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo",
        }

    def test_invalid_data(self, invalid_data):
        response, status_code = register(**invalid_data, Model=UserModel)

        assert status_code == 400
        assert min_length_message(NAME_MIN_LENGTH) in response.get("name")
        assert max_length_message(EMAIL_MAX_LENGTH) and email_message() in response.get(
            "email"
        )

    def test_max_name_length(self, valid_data):
        response, status_code = register(
            name="ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo",
            email=valid_data.get("email"),
            Model=UserModel,
        )

        assert status_code == 400
        assert {"name": max_length_message(NAME_MAX_LENGTH)} == response

    def test_valid_data(self, valid_data):
        response, status_code = register(**valid_data, Model=UserModel)

        assert status_code == 200
        assert response == {**valid_data, "id": 999}
