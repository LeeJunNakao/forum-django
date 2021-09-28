from django.contrib.auth.models import User as UserBase

USERNAME_MIN_LENGTH = 5
USERNAME_MAX_LENGTH = 30
EMAIL_MAX_LENGTH = 40


class User(UserBase):
    def as_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
