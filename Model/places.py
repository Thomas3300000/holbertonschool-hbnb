#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User
from city import City
""" A class named Place that defines a place. """


class Place:
    """ Initilizes a new place. """
    def __init__(self, place_id, name, description, address, city, latitude, longitude, host, num_rooms, num_bathrooms, price_per_night, max_guests):
        """
        Initializes a new place.

        Args:
            place_id (uuid4) : The identifier of the place.
            name (str): The name of the place.
            description (str): The description of the place.
            address (str): The adress of the place.
            city (City): The city where is the place.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            host (User): The user who hosts the place.
            num_rooms (int): The number of rooms.
            num_bathrooms (int): The number of bathrooms.
            price_per_night (float): The price per night.
            max_guests (int): The maximum number of people who can live in.
        """
        self.place_id = uuid.uuid4()
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

        #host.add_place(self)

    """ A method that adds new amenities. """
    @add_amenity.setter
    def add_amenity(self, amenity):
        """ A method that adds new amenities. """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    """ A method that adds new reviews. """
    @add_review.setter
    def add_review(self, review):
        """ A method that adds new reviews. """
        self.reviews.append(review)

    """ A method that displays a comprehensive message for the user. """
    def __str__(self):
        """ Returns the name of the place and the city. """
        return f"{self.name} in {self.city.name}, {self.city.country.name}"
