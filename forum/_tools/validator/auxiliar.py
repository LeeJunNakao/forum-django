from typing import Dict, List

errors_list = List[str]


def filter_valid_items_list(li: List[str]) -> List[str]:
    return [item for item in li if item]


def get_errors(**errors_info: errors_list):
    errors_info = {
        key: filter_valid_items_list(value) for key, value in errors_info.items()
    }
    errors = {key: ", ".join(value)
              for key, value in errors_info.items() if value}

    return errors
