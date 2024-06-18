from uuid import uuid4
from datetime import datetime

""" A class named Amenity that defines an amenity. """


class Amenity:
    def __init__(self, name):
        self.amenity_id = uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """ A method that gets the amenity_id. """
    @property
    def amenity_id(self):
        return self._amenity_id

    """ A method that defines the value of the amenity_id. """
    @amenity_id.setter
    def amenity_id(self, value):
        self._amenity_id = value

    """ A method that gets the name. """
    @property
    def name(self):
        return self._name

    """ A method that defines the value of the name. """
    @name.setter
    def name(self, value):
        self._name = value

    """ A method that defines the update time. """
    def update_at(self, new_name):
        self.name = new_name
        self.updated_at = datetime.now()

