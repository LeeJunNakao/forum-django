import pytest
from authentication.services.auth import (
    register,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
    EMAIL_MAX_LENGTH,
)
from _tools.validator.message_error import (
    max_length_message,
    min_length_message,
    email_message,
)


class TestUserServiceRegister:
    @pytest.fixture
    def valid_data(self):
        return {"username": "Valid Name", "email": "valid_email@email.com"}

    @pytest.fixture
    def invalid_data(self):
        return {
            "username": "sd",
            "email": "ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo",
        }

    def test_invalid_data(self, invalid_data, user_model):
        response, status_code = register(**invalid_data, Model=user_model)

        assert status_code == 400
        assert min_length_message(USERNAME_MIN_LENGTH) in response.get("username")
        assert max_length_message(EMAIL_MAX_LENGTH) and email_message() in response.get(
            "email"
        )

    def test_max_name_length(self, valid_data, user_model):
        response, status_code = register(
            name="ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo",
            email=valid_data.get("email"),
            Model=user_model,
        )

        assert status_code == 400
        assert {"username": max_length_message(USERNAME_MAX_LENGTH)} == response

    def test_valid_data(self, valid_data, user_model):
        response, status_code = register(**valid_data, Model=user_model)

        assert status_code == 200
        assert response == {**valid_data, "id": 999}
