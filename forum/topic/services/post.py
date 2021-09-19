from typing import Type
from _tools.validator.auxiliar import get_errors
from _tools.validator.fns import validate_max_length, validate_min_lenght
from topic.models import (
    PostModel,
    TITLE_MAX_LENGTH,
    TITLE_MIN_LENGTH,
    CONTENT_MIN_LENGTH,
    CONTENT_MAX_LENGTH,
)


def create(
    title: str,
    content: str,
    creator_id: int,
    topic_id: int,
    post_model: Type[PostModel],
):
    errors = get_errors(
        title=[
            validate_min_lenght(title, TITLE_MIN_LENGTH),
            validate_max_length(title, TITLE_MAX_LENGTH),
        ],
        content=[
            validate_min_lenght(content, CONTENT_MIN_LENGTH),
            validate_max_length(content, CONTENT_MAX_LENGTH),
        ],
    )

    if len(errors):
        return errors, 400

    post = post_model(
        title=title, content=content, creator_id=creator_id, topic_id=topic_id
    )
    post.save()

    return post.as_dict(), 200
