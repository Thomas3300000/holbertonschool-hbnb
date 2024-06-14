from uuid import uuid4
from datetime import datetime

class Amenity:
    def __init__(self, name):
        self.amenity_id = uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def amenity_id(self):
        return self._amenity_id
    
    @amenity_id.setter
    def amenity_id(self, value):
        self._amenity_id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def update_at(self, new_name):
        self.name = new_name
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Amenity: {self.name}"