from typing import Any, Dict
from django.db import models
from authentication.models import User

TITLE_MAX_LENGTH = 40
TITLE_MIN_LENGTH = 3
CONTENT_MAX_LENGTH = 1000
CONTENT_MIN_LENGTH = 1


class TopicModel(models.Model):
    class Meta:
        verbose_name = "Topic"

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def as_dict(self) -> Dict[str, Any]:
        posts = [post.related_as_dict() for post in self.posts.all()]
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "creator": self.creator.as_dict(),
            "posts": posts,
            "posts_quantity": len(posts),
            "created_at": self.created_at.strftime("%s")
        }


class PostModel(models.Model):
    class Meta:
        verbose_name = "Post"

    content = models.TextField()
    topic = models.ForeignKey(
        TopicModel, related_name="posts", on_delete=models.CASCADE
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "content": self.content,
            "topic": self.topic.as_dict(),
            "creator": self.creator.as_dict(),
            "created_at": self.created_at.strftime("%s"),
        }

    def related_as_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "content": self.content,
            "creator": self.creator.as_dict(),
            "created_at": self.created_at.strftime("%s"),
        }
