from django.db import models

NAME_MIN_LENGTH = 5
NAME_MAX_LENGTH = 30
EMAIL_MAX_LENGTH = 40


class User(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.CharField(max_length=EMAIL_MAX_LENGTH)

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
