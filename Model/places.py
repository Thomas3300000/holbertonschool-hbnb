from uuid import uuid4
from datetime import datetime
from Model.user import User
from Model.city import City
from Model.country import Country
from Model.amenities import Amenity
from Model.review import Review
""" A class named Place that defines a place. """


class Place:
    def __init__(self, place_id, name, description, address, city, latitude,
                 longitude, host, num_rooms, num_bathrooms, price_per_night,
                 max_guests):
        self.place_id = place_id
        self._name = name
        self._description = description
        self._address = address
        self._city = city
        self._latitude = latitude
        self._longitude = longitude
        self._host = host
        self._num_rooms = num_rooms
        self._num_bathrooms = num_bathrooms
        self._price_per_night = price_per_night
        self._max_guests = max_guests
        self.amenities = []
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def num_rooms(self):
        return self._num_rooms

    @num_rooms.setter
    def num_rooms(self, value):
        self._num_rooms = value

    @property
    def num_bathrooms(self):
        return self._num_bathrooms

    @num_bathrooms.setter
    def num_bathrooms(self, value):
        self._num_bathrooms = value

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        self._price_per_night = value

    @property
    def max_guests(self):
        return self._max_guests

    @max_guests.setter
    def max_guests(self, value):
        self._max_guests = value

    """ A method that gets the amenities. """
    @property
    def get_amenity(self, amenity_id):
        """ Gets a amenity if it has an id. """
        for amenity in self.amenities:
            if amenity.amenity_id == amenity_id:
                return amenity
        return None

    """ A method that returns the list of amenities. """
    @property
    def list_amenities(self):
        """ Returns the list of amenities. """
        return self.amenities

    """ A method that adds new amenities. """

    def add_amenity(self, amenity):
        """ Adds a new amenity if not in the list. """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    """ A method that adds new reviews. """

    def add_review(self, review):
        """ Adds a new review. """
        self.reviews.append(review)

    """ A method that returns the list of reviews. """
    @property
    def list_reviews(self):
        """ Returns the list of reviews. """
        return self.reviews

    """ A method that gets the reviews. """
    @property
    def get_review(self, review_id):
        """ Gets a review if it has an id. """
        for review in self.reviews:
            if review.review_id == review_id:
                return review
        return None

    """ A method that displays a comprehensive message for the user. """
    def __str__(self):
        """ Returns the name of the place and the city. """
        return f"{self.name} in {self.city.name}, {self.city.country.name}"
