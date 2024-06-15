import unittest
from datetime import datetime
from uuid import uuid4
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.amenities import Amenity
from Model.places import Place
from Model.city import City
from Model.country import Country
from Model.user import User


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.country = Country(name="France", code="FR")
        self.city = City(name="Paris", country=self.country)
        self.user = User("Joe", "Seulympik", "joe@example.com", "password789")
        self.place = Place(
            place_id=uuid4(),
            name="Sportive House",
            description="A house in Paris during Olympic Games",
            address="123, Rue de la Seine",
            city=self.city,
            latitude=48.8566,
            longitude=2.3522,
            host=self.user,
            num_rooms=3,
            num_bathrooms=2,
            price_per_night=200,
            max_guests=6
        )
        self.amenity = Amenity(name="WiFi")

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_add_amenity_to_place(self):
        self.place.add_amenity(self.amenity)
        self.assertIn(self.amenity, self.place.amenities)
        self.amenity.add_amenity("Pool")
        self.assertIn("Pool", self.amenity.list_amenities())

    def test_update_amenity(self):
        new_name = "High-speed WiFi"
        self.amenity.name = new_name
        self.amenity.updated_at = datetime.now()
        self.assertEqual(self.amenity.name, new_name)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_get_amenity(self):
        self.place.add_amenity(self.amenity)
        retrieved_amenity = self.place.get_amenity(self.amenity.name)
        self.assertEqual(retrieved_amenity.name, self.amenity.name)

    def test_amenity_deletion(self):
        self.place.add_amenity(self.amenity)
        self.place.remove_amenity(self.amenity)
        self.assertNotIn(self.amenity, self.place.amenities)


if __name__ == "__main__":
    unittest.main()
