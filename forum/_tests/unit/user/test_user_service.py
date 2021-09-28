from operator import itemgetter
from toolz import assoc
import pytest
from authentication.services.auth import (
    register,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
    EMAIL_MAX_LENGTH,
)
from authentication.models import User
from _tools.validator.message_error import (
    max_length_message,
    min_length_message,
    email_message,
    password_message
)


class TestUserServiceRegister:
    @pytest.fixture
    def valid_data(self):
        return {"username": "Valid Name", "email": "valid_email@email.com", "password": "Password526&"}

    @pytest.fixture
    def invalid_data(self):
        return {
            "username": "sd",
            "email": "ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo",
            "password": "password"
        }
    
    @pytest.fixture
    def user_model(self, mock_module, mock_function):
        def set_response(expected_response = None):
            model = mock_module("UserModel", User)
            model.as_dict = mock_function("UserModel.as_dict", expected_response)

            return mock_function("UserModel init", model)
        
        return set_response
            

    def test_invalid_data(self, invalid_data, user_model):
        response, status_code = register(**invalid_data, user_model=user_model())

        assert status_code == 400
        assert min_length_message(USERNAME_MIN_LENGTH) in response.get("username")
        assert max_length_message(EMAIL_MAX_LENGTH) and email_message() in response.get(
            "email"
        )
        assert response.get("password") == password_message()

    def test_max_name_length(self, valid_data, user_model):
        username = "ldkasdkadokasdkasdopakdopaskdpoasdpoaskdpokasdpoksadpo"

        response, status_code = register(
            **assoc(valid_data, "username", username),
            user_model=user_model,
        )

        assert status_code == 400
        assert {"username": max_length_message(USERNAME_MAX_LENGTH)} == response

    def test_valid_data(self, valid_data, user_model):
        response, status_code = register(**valid_data, user_model=user_model(valid_data))

        assert status_code == 200
        assert response == valid_data
