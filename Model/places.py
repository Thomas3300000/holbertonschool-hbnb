from uuid import uuid4
from datetime import datetime
from user import User
from city import City
from country import Country
from amenities import Amenity
from review import Review
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

        host.add_place(self)

    @property
    def place_id(self):
        return self.place_id
    
    @place_id.setter
    def place_id(self, value):
        self.place_id = value

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self.name = value

    @property
    def description(self):
        return self.description
    
    @description.setter
    def description(self, value):
        self.description = value

    @property
    def address(self):
        return self.address
    
    @address.setter
    def address(self, value):
        self.address = value

    @property
    def city(self):
        return self.city
    
    @city.setter
    def city(self, value):
        self.city = value

    @property
    def lattitude(self):
        return self.lattitude
    
    @lattitude.setter
    def lattitude(self, value):
        self.lattitude = value

    @property
    def longitude(self):
        return self.longitude
    
    @longitude.setter
    def longitude(self, value):
        self.longitude = value

    @property
    def host(self):
        return self.host
    
    @host.setter
    def host(self, value):
        self.host = value
    
    @property
    def num_rooms(self, value):
        self.num_rooms = value

    @num_rooms.setter
    def num_rooms(self, value):
        self.num_rooms = value

    @property
    def num_bathrooms(self):
        return self.num_bathrooms
    
    @num_bathrooms.setter
    def num_bathrooms(self, value):
        self.num_bathrooms = value

    @property
    def price_per_night(self):
        return self.price_per_night
    
    @price_per_night.setter
    def price_per_night(self, value):
        self.price_per_night = value

    @property
    def max_guests(self):
        return self.max_guests
    
    @host.setter
    def max_guests(self, value):
        self.max_guests = value

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
    @add_amenity.setter
    def add_amenity(self, amenity):
        """ Adds a new amenity if not in the list. """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    """ A method that adds new reviews. """
    @add_review.setter
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
