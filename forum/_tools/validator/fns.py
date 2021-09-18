import re
from typing import Sized
from _tools.validator.message_error import max_length_message, min_length_message, email_message


def validate_max_length(value: Sized, limit: int) -> str:
    is_not_valid = len(value) > limit
    return max_length_message(limit) if is_not_valid else ''


def validate_min_lenght(value: Sized, limit: int) -> str:
    is_not_valid = len(value) < limit
    return min_length_message(limit) if is_not_valid else ''


def validate_email(value: str) -> str:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return email_message() if not re.fullmatch(regex, value) else ''
