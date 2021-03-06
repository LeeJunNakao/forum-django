from typing import Type
from django.db import Error, IntegrityError
from _tools.validator.auxiliar import get_errors
from _tools.validator.fns import validate_max_length, validate_min_lenght
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist
from topic.models import (
    TITLE_MAX_LENGTH,
    TITLE_MIN_LENGTH,
    CONTENT_MIN_LENGTH,
    CONTENT_MAX_LENGTH,
)


def create(
    content: str,
    creator_id: int,
    topic_id: int,
    topic_model: Type[Model],
    post_model: Type[Model],
):

    try:
        errors = get_errors(
            content=[
                validate_min_lenght(content, CONTENT_MIN_LENGTH),
                validate_max_length(content, CONTENT_MAX_LENGTH),
            ],
        )

        if len(errors):
            return errors, 400

        topic_model.objects.get(pk=topic_id)
        post = post_model(
            content=content, creator_id=creator_id, topic_id=topic_id
        )
        post.save()

        return post.as_dict(), 200

    except (IntegrityError, ObjectDoesNotExist, Error):
        return {"error": "Could not create topic"}, 400
