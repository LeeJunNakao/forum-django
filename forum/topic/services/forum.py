from typing import Any, Dict, List, Tuple, Union
from django.db.models import Model
from django.db import Error

topics_dict = List[Dict[str, Any]]
response_data = Tuple[Any, int]


def get_all_topics(
    topic_model: Model,
) -> Tuple[Union[topics_dict, Dict[str, Any]], int]:
    try:
        topics = topic_model.objects.all()
        return [topic.as_dict() for topic in topics], 200
    except Error:
        return {"error": "Failed to get topic"}, 400
