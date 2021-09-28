from typing import Dict, Tuple, Type
from django.db.models import Model
from authentication.models import (
    USERNAME_MIN_LENGTH,
    USERNAME_MAX_LENGTH,
    EMAIL_MAX_LENGTH,
)
from django.db import Error
from _tools.validator.fns import (
    validate_max_length,
    validate_min_lenght,
    validate_email,
    validate_password,
)
from _tools.validator.auxiliar import get_errors


def register(
    username: str, email: str, password: str, user_model: Type[Model]
) -> Tuple[Dict[str, str], int]:
    try:
        errors = get_errors(
            username=[
                validate_min_lenght(username, USERNAME_MIN_LENGTH),
                validate_max_length(username, USERNAME_MAX_LENGTH),
            ],
            email=[validate_max_length(email, EMAIL_MAX_LENGTH), validate_email(email)],
            password=[validate_password(password)],
        )

        if len(errors):
            return errors, 400

        user = user_model(username=username, email=email, password=password)
        user.save()
        return user.as_dict(), 200

    except Error:
        return {"error": "Could not register user"}, 400
