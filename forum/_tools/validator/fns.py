import re
from typing import Sized
from _tools.validator.message_error import (
    max_length_message,
    min_length_message,
    email_message,
    password_message,
)


def validate_max_length(value: Sized, limit: int) -> str:
    is_not_valid = len(value) > limit
    return max_length_message(limit) if is_not_valid else ""


def validate_min_lenght(value: Sized, limit: int) -> str:
    is_not_valid = len(value) < limit
    return min_length_message(limit) if is_not_valid else ""


def validate_email(value: str) -> str:
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return email_message() if not re.fullmatch(regex, value) else ""

def validate_password(value: str) -> str:
    has_lower_case = re.search('[a-z]', value)
    has_upper_case = re.search('[A-Z]', value)
    has_number = re.search('[0-9]', value)
    has_special_char = re.search(r'\W', value)
    min_length = len(value) >= 8
    max_length = len(value) <= 20

    is_valid = has_lower_case and has_upper_case and has_number and has_special_char and min_length and max_length

    return password_message() if not bool(is_valid) else ""


