from uuid import uuid4
from datetime import datetime
from Model.user import User


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

    """ A method that gets the name. """
    @property
    def name(self):
        return self._name

    """ A method that defines the value of the name. """
    @name.setter
    def name(self, value):
        self._name = value

    """ A method that gets the description. """
    @property
    def description(self):
        return self._description

    """ A method that defines the value of the description. """
    @description.setter
    def description(self, value):
        self._description = value

    """ A method that gets the address. """
    @property
    def address(self):
        return self._address

    """ A method that defines the value of the address. """
    @address.setter
    def address(self, value):
        self._address = value

    """ A method that gets the city. """
    @property
    def city(self):
        return self._city

    """ A method that defines the value of the city. """
    @city.setter
    def city(self, value):
        self._city = value

    """ A method that gets the lattitude. """
    @property
    def latitude(self):
        return self._latitude

    """ A method that defines the value of the lattitude. """
    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    """ A method that gets the longitude. """
    @property
    def longitude(self):
        return self._longitude

    """ A method that defines the value of the longitude. """
    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    """ A method that gets the host. """
    @property
    def host(self):
        return self._host

    """ A method that defines the value of the host. """
    @host.setter
    def host(self, value):
        if not isinstance(value, User):
            raise ValueError("Host must be a User instance")
        self._host = value

    """ A method that gets the number of rooms. """
    @property
    def num_rooms(self):
        return self._num_rooms

    """ A method that defines the value of the number of rooms. """
    @num_rooms.setter
    def num_rooms(self, value):
        self._num_rooms = value

    """ A method that gets the number of bathrooms. """
    @property
    def num_bathrooms(self):
        return self._num_bathrooms

    """ A method that defines the value of the number of bathrooms. """
    @num_bathrooms.setter
    def num_bathrooms(self, value):
        self._num_bathrooms = value

    """ A method that gets the price per night. """
    @property
    def price_per_night(self):
        return self._price_per_night

    """ A method that defines the value of the price per night. """
    @price_per_night.setter
    def price_per_night(self, value):
        self._price_per_night = value

    """ A method that gets the max number of guests. """
    @property
    def max_guests(self):
        return self._max_guests

    """ A method that defines the value of the max number of guests. """
    @max_guests.setter
    def max_guests(self, value):
        self._max_guests = value

    """ A method that gets the amenities. """
    @property
    def get_amenity(self, amenity_id):
        """ Gets a amenity if it has an id. """
        for amenity in self.amenities:
            if amenity == amenity_id:
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

    def remove_amenity(self, amenity):
        """ Removes an amenity if it presents in the list. """
        if amenity in self.amenities:
            self.amenities.remove(amenity)

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
            if review == review_id:
                return review
        return None

