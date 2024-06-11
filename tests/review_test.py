import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.review import Review
from models.user import User
from models.place import Place
from uuid import UUID



class TestReview(unittest.TestCase):
    def set_up(self):
        self.user = User("Carlos", "Santane", "carlos.santana@example.com")
        self.place1 = Place("House Dreams")
        self.place2 = Place("Joy House")
        self.review = Review(self.user, 5, self.place1, "Amazing place!")

    def test_review_creation(self):
        self.assertIsInstance(self.review.id, UUID)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.place, self.place1)
        self.assertEqual(self.review.comment, "Amazing place!")
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.review.rating = 6

    def test_invalid_place(self):
        invalid_place = Place("Invalid Place")
        Place.places.remove(invalid_place)
        with self.assertRaises(ValueError):
            self.review.place = invalid_place

    def test_update_review(self):
        self.review.update(rating=4, comment="Good place.")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Good place.")
        self.assertNotEqual(self.review.updated_at, self.review.created_at)

    def test_delete_review(self):
        self.review.delete_review()
        self.assertNotIn(self.review, Review.review)

    def test_empty_comment(self):
        with self.assertRaises(ValueError):
            self.review.comment = ""

if __name__ == "__main__":
    unittest.main()