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


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.country = "France"
        self.city = "Bordeaux"
        self.user = "Betty Holberton"
        self.place = Place(
            place_id=uuid4(),
            name="Little House",
            description="A little house in Bordeaux",
            address="123 Rue de Bordeaux",
            city=self.city,
            latitude=8.8566,
            longitude=42.3522,
            host=self.user,
            num_rooms=1,
            num_bathrooms=1,
            price_per_night=100,
            max_guests=2
        )

    def test_place_creation(self):
        self.assertEqual(self.place.name, "Little House")
        self.assertEqual(self.place.city, self.city)
        self.assertEqual(self.place.host, self.user)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    #def test_single_host_assignment(self):
    #    new_user = "Betty Holberton"
    #    with self.assertRaises(ValueError):
    #        self.place.host = new_user

    def test_valid_coordinates(self):
        self.assertTrue(-90 <= self.place.latitude <= 90)
        self.assertTrue(-180 <= self.place.longitude <= 180)

    def test_valid_price_and_guests(self):
        self.assertTrue(self.place.price_per_night > 0)
        self.assertTrue(self.place.max_guests > 0)

    #def test_place_deletion(self):
    #    self.user.remove_place(self.place)
    #    self.assertNotIn(self.place, self.user.hosted_places)

    def test_add_amenity(self):
        amenity = "WiFi"
        self.place.add_amenity(amenity)
        self.assertIn(amenity, self.place.amenities)
        self.place.add_amenity(amenity)
        self.assertEqual(len(self.place.amenities), 1)

    def test_add_review(self):
        review = "Great place!"
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)

    def test_update_amenity(self):
        amenity = "WiFi"
        self.place.add_amenity(amenity)
        self.place.amenities.remove(amenity)
        self.place.add_amenity("Pool")
        self.assertNotIn(amenity, self.place.amenities)
        self.assertIn("Pool", self.place.amenities)


if __name__ == "__main__":
    unittest.main()
