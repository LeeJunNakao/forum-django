from typing import Any, Dict
from django.db import models
from authentication.models import User

TITLE_MAX_LENGTH = 40
TITLE_MIN_LENGTH = 3


class TopicModel(models.Model):
    class Meta:
        verbose_name = "Topic"

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def as_dict(self) -> Dict[str, Any]:
        return {"title": self.title, "creator": self.creator.as_dict()}
