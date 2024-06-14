from typing import List  # Import types for list annotations
from Model.city import City  # Import the City class


class Country:
    """A class to represent a country
    Attributes:
    name : str
        The name of the country.
    cities : List[City]
        A list of cities in the country"""

    def __init__(self, name: str, cities: List[City] = None):
        """
        Initialize a Country object with a name and an optional list of cities
        Parameters:
        name : str
        The name of the country
        cities : List[City],
            A list of cities in the country
            (default is None, which initializes an empty list)"""
        self.name = name  # Assign the country name
        self.cities = cities or []  # Initialize the list of cities

    @property
    def name(self):
        """str: Get or set the name of the country"""
        return self.__name  # Return the country name

    @name.setter
    def name(self, value):
        """Set the name of the country
        Parameters:
        value : str
        The new name of the country
        Raises:
        TypeError: If the value is not a string"""
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value  # Assign the value to the private attribute __name

    def add_city(self, city: City):
        """Add a city to the country's list of cities
        Parameters:
        city : City
            The city to add
            Raises:
        ValueError:
            If the city is already in the list"""
        if city in self.cities:
            raise ValueError(f"City {city.name} already added to this country")
        self.cities.append(city)  # Add the city to the list

    def get_all_cities(self):
        """Get a list of all cities in the country
        Returns:
        list of City: The list of all cities"""
        return list(self.cities)  # Return the list of all cities