from typing import Type
from django.db import Error
from _tools.validator.auxiliar import get_errors
from _tools.validator.fns import validate_max_length, validate_min_lenght
from topic.models import TopicModel, TITLE_MAX_LENGTH, TITLE_MIN_LENGTH


def create(title: str, user_id: int, content: str, model: Type[TopicModel]):
    try:
        errors = get_errors(
            title=[
                validate_max_length(title, TITLE_MAX_LENGTH),
                validate_min_lenght(title, TITLE_MIN_LENGTH),
            ]
        )

        if len(errors):
            return errors, 400

        topic = model(title=title, content=content, creator_id=user_id)
        topic.save()

        return topic.as_dict(), 200
    except Error:
        return {"error": "Could not create topic"}, 400


def get(id_: int, model: Type[TopicModel]):
    try:
        return model.objects.get(pk=id_).as_dict(), 200
    except:
        return {"error": "Could not get topic"}, 400
