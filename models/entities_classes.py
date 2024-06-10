#!/usr/bin/python3
import uuid
from datetime import datetime
""" ..."""


class User:
    """..."""
    def __init__(self, user_id, email, password, first_name, last_name):
        """..."""
        self.user_id = user_id.uuid4()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.hosted_places = []
        self.reviews = []
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    """..."""
    def register(self, email):
        """..."""
        self.email.append(email)

    """..."""
    def login(self, first_name, last_name):
        """..."""
        pass

    """..."""
    def logout(self, first_name, last_name):
        """..."""
        pass

    """..."""
    def add_place(self, place):
        """..."""
        self.hosted_places.append(place)

    """..."""
    def add_review(self, review):
        """..."""
        self.reviews.append(review)

    """..."""
    def __str__(self):
        """..."""
        return f"{self.first_name} {self.last_name} : {self.email}"


"""..."""


class Place:
    """..."""
    def __init__(self, place_id, name, description, address, city, latitude, longitude, host, num_rooms, num_bathrooms, price_per_night, max_guests):
        """..."""
        self.place_id = place_id.uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        self.reviews = []
        self.created_at = datetime.now()
        self.update_at = datetime.now()

        host.add_place(self)

    """..."""
    def add_amenity(self, amenity):
        """..."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    """..."""
    def add_review(self, review):
        """..."""
        self.reviews.append(review)

    """..."""
    def __str__(self):
        """..."""
        return f"{self.name} in {self.city.name}, {self.city.country.name}"


"""..."""


class City:
    """..."""
    def __init__(self, city_id, name, country):
        """..."""
        self.city_id = city_id.uuid4()
        self.name = name
        self.country = country
        self.places = []
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    """..."""
    def add_place(self, place):
        """..."""
        self.places.append(place)

    """..."""
    def __str__(self):
        """..."""
        return f"{self.name}, {self.country.name}"


"""..."""


class Country:
    """..."""
    def __init__(self, name):
        """..."""
        self.name = name
        self.cities = []

    """..."""
    def add_city(self, city):
        """..."""
        self.cities.append(city)

    """..."""
    def __str__(self):
        """..."""
        return f"{self.name} ({self.code})"
