from uuid import uuid4
from datetime import datetime
from user import User
from places import Place


class Review:
    review = []

    def __init__(self, user: User, rating: int, place: Place, comment: str):
        self.id = uuid4()
        self.user = user
        self.rating = rating
        self.place = place
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Review.review.append(self)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if value not in Place.places:
            raise ValueError(f"{value} is not a valid place")
        self._place = value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def delete_review(self):
        Review.review.remove(self)
