def max_length_message(limit: int) -> str:
    return f"value is greater than {limit}"


def min_length_message(limit: int) -> str:
    return f"value is lower than {limit}"


def email_message() -> str:
    return "should be a valid email"


def password_message() -> str:
    return "password must have a number, lower case, upper case and a special char"
