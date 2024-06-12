import uuid  # Importing uuid module for generating unique city IDs
from datetime import datetime  # Importing datetime for timestamps


class City:
    _cities = []  # Class variable to store all city instances

    def __init__(self, name: str):
        """Initializes a new City instance
        :param name: The name of the city
        :raises ValueError: If the city already exists"""
        existing_city = self.get_city_by_name(name)  # Check if city exists
        if existing_city:
            raise ValueError(f"The city '{name}' already exists")
        else:
            self.city_id = uuid.uuid4()  # Generate unique city ID
            self.name = name  # Set city name
            self.created_at = datetime.now()  # Set creation timestamp
            self.updated_at = datetime.now()  # Set updated timestamp
            self.add_city()  # Add city to the list

    def add_city(self):
        """Adds the current city instance to the list of cities"""
        City._cities.append({  # Append city details to the list
            'created_at': self.created_at,  # Add creation timestamp
            'updated_at': self.updated_at,  # Add updated timestamp
            'city_id': self.city_id,  # Add city ID
            'name': self.name,  # Add city name
        })

    @property
    def name(self):
        """Gets the name of the city"""
        return self._name  # Return the name of the city

    @name.setter
    def name(self, value: str):
        """Sets the name of the city
        :param value: The new name of the city
        :raises TypeError: If the name is not a non-empty string"""
        if not isinstance(value, str) or not value:
            raise TypeError("The name must be a non-empty string")
        self._name = value  # Set the new name

    @property
    def created_at(self):
        """Gets the creation time of the city"""
        return self._created_at  # Return the creation timestamp

    @created_at.setter
    def created_at(self, value):
        """Sets the creation time of the city
        :param value: The new creation time
        :raises TypeError: If the value is not a datetime instance"""
        if not isinstance(value, datetime):
            raise TypeError("created_at must be a datetime instance")
        self._created_at = value  # Set the creation timestamp

    @property
    def updated_at(self):
        """Gets the last updated time of the city"""
        return self._updated_at  # Return the updated timestamp

    @updated_at.setter
    def updated_at(self, value):
        """Sets the last updated time of the city
        :param value: The new updated time
        :raises TypeError: If the value is not a datetime instance"""
        if not isinstance(value, datetime):
            raise TypeError("updated_at must be a datetime instance")
        self._updated_at = value  # Set the updated timestamp

    @classmethod
    def get_all_cities(cls):
        """Returns a list of all cities"""
        return cls._cities  # Return the list of all cities

    @staticmethod
    def get_city_by_name(name: str):
        """Gets a city by its name
        :param name: The name of the city
        :return: The city with the given name, or None if not found"""
        for city in City._cities:  # Iterate over the list of cities
            if city['name'] == name:  # Check if name matches
                return city  # Return the matching city
        return None  # Return None if no city is found

    def update(self, **kwargs):
        """Updates the city's attributes
        :param kwargs: The attributes to update"""
        for key, value in kwargs.items():  # Iterate over the kwargs
            if key in ['name']:  # Check if the key is 'name'
                setattr(self, key, value)  # Set the new value
        self.updated_at = datetime.now()  # Update the timestamp
        for city in City._cities:  # Iterate over the list of cities
            if city['city_id'] == self.city_id:  # Check if ID matches
                city['name'] = self.name  # Update the name
                city['updated_at'] = self.updated_at  # Update timestamp
                break  # Exit the loop after update
