from typing import Dict, Tuple, Type
from authentication.models import (
    User,
    NAME_MIN_LENGTH,
    NAME_MAX_LENGTH,
    EMAIL_MAX_LENGTH,
)
from django.db import Error
from _tools.validator.fns import (
    validate_max_length,
    validate_min_lenght,
    validate_email,
)
from _tools.validator.auxiliar import get_errors


def register(name: str, email: str, Model: Type[User]) -> Tuple[Dict[str, str], int]:
    try:
        errors = get_errors(
            name=[
                validate_min_lenght(name, NAME_MIN_LENGTH),
                validate_max_length(name, NAME_MAX_LENGTH),
            ],
            email=[validate_max_length(email, EMAIL_MAX_LENGTH), validate_email(email)],
        )

        if len(errors):
            return errors, 400

        user = Model(name=name, email=email)
        user.save()
        return user.as_dict(), 200

    except Error:
        return {"error": "Could not register user"}, 400
