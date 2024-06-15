import unittest
from datetime import datetime
from uuid import uuid4
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.amenities import Amenity
from Model.places import Place


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity(name="WiFi")
        self.place = Place(
            place_id=uuid4(),
            name="Dream House",
            description="A little house in Bordeaux",
            address="123 Rue de Bordeaux",
            city="Bordeaux",
            latitude=8.8566,
            longitude=42.3522,
            host="Dave Loppeur",
            num_rooms=1,
            num_bathrooms=1,
            price_per_night=100,
            max_guests=2
        )

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_add_amenity_to_place(self):
        self.place.add_amenity(self.amenity)
        self.assertIn(self.amenity, self.place.amenities)
        self.place.add_amenity("Pool")
        self.assertIn("Pool", self.place.amenities)

    def test_update_amenity(self):
        new_name = "Pool and Tobogan"
        self.amenity.name = new_name
        self.amenity.updated_at = datetime.now()
        self.assertEqual(self.amenity.name, new_name)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    #def test_get_amenity(self):
    #    self.place.add_amenity(self.amenity)
    #    retrieved_amenity = self.place.get_amenity(self.amenity.name)
    #    self.assertEqual(retrieved_amenity, self.amenity.name)

    def test_amenity_deletion(self):
        self.place.add_amenity(self.amenity)
        self.place.remove_amenity(self.amenity)
        self.assertNotIn(self.amenity, self.place.amenities)


if __name__ == "__main__":
    unittest.main()
