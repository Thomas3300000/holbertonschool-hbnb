import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.review import Review
from Model.places import Place
from uuid import UUID


class TestReview(unittest.TestCase):

    def setUp(self):
        self.place = Place("House of dream", "Amazing place to stay",
                           "123 Main St", "San Francisco", 37.7749, -122.4194,
                           "Host Name", 3, 2, 200, 4, 6)

        self.review = Review(self.place, 5, "House of dream",
                             "Great experience!")

    def tearDown(self):
        Review.review.clear()

    def test_review_creation(self):
        self.assertIsInstance(self.review.id, UUID)
        self.assertEqual(self.review.place, "House of dream")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great experience!")
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_update_review(self):
        self.review.update(rating=4, comment="Good place.")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Good place.")
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.review.rating = 6


    
    #def test_delete_review(self):
    #   self.assertIn(self.review, self.place.reviews)
    #   self.place.reviews = [review for review in self.place.reviews if review != self.review]
    #    self.assertNotIn(self.review, self.place.reviews)
        
    #def test_empty_comment(self):
    #    with self.assertRaises(ValueError):
    #        self.review.update(comment ="")


def test_invalid_place(self):
    with self.assertRaises(TypeError):
        invalid_place = Place("Invalid Place")


if __name__ == '__main__':
    unittest.main()
