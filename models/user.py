from datetime import datetime
from review import Review
from places import Places
from uuid import uuid4


class User:
    _registered_emails = set()
    users = []

    def __init__(self, first_name, last_name, email, password):
        if email in User._registered_emails:
            raise ValueError(f"{email} already registered")
        self.id = uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.places = []
        User.users.append(self)
        User._registered_emails.add(email)

    def change_password(self, new_password):
        self.password = new_password
        self.updated_at = datetime.now()

    def check_password(self, password):
        return self.password == password

    def add_review(self, review: Review):
        if review in self.reviews:
            self.reviews.append(review)
            self.updated_at = datetime.now()

    def remove_review(self, review):
        self.reviews.remove(review)
        self.updated_at = datetime.now()

    def add_place(self, place):
        if place in self.places:
            self.places.append(place)
            self.updated_at = datetime.now()

    def remove_place(self, places):
        self.places.remove(places)
        self.updated_at = datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == "email":
                    if value in User._registered_emails:
                        raise ValueError(f"{value} already registered")
                    User._registered_emails.remove(self.email)
                    User._registered_emails.add(value)
                setattr(self, key, value)
        self.updated_at = datetime.now()

    @staticmethod
    def get_by_id(user_id):
        for user in User.users:
            if user.id == user_id:
                return user
        return ("User not found")

    @staticmethod
    def get_by_email(email):
        for user in User.users:
            if user.email == email:
                return user
        return ("User not found")

    @staticmethod
    def delete_user(user_id):
        user = User.get_by_id(user_id)
        if user:
            User._registered_emails.remove(user.email)
            User.users.remove(user)
