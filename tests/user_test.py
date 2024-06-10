import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User


class TestUser(unittest.TestCase):
    def create_user_test(self):
        self.user = User("Carlos", "Santana", "carlos@example.com", "password123")

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "Carlos")
        self.assertEqual(self.user.last_name, "Santana")
        self.assertEqual(self.user.email, "carlos@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(len(User.users), 1)
        self.assertIn(self.user, User.users)
        self.assertIn("carlos@example.com", User._registered_emails)

    def test_change_password(self):
        self.user.change_password("newpassword123")
        self.assertEqual(self.user.password, "newpassword123")
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_check_password(self):
        self.assertTrue(self.user.check_password("password123"))
        self.assertFalse(self.user.check_password("123password"))

    def test_add_review(self):
        review = "Great place to stay!"
        self.user.add_review(review)
        self.assertIn(review, self.user.reviews)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_remove_review(self):
        review = "Good place for chilling"
        self.user.add_review(review)
        self.user.remove_review(review)
        self.assertNotIn(review, self.user.reviews)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_add_place(self):
        place = "House dreams"
        self.user.add_place(place)
        self.assertIn(place, self.user.places)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_remove_place(self):
        place = "House dreams"
        self.user.add_place(place)
        self.user.remove_place(place)
        self.assertNotIn(place, self.user.places)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_update(self):
        new_email = "carlos.santana@example.com"
        self.user.update(email=new_email)
        self.assertEqual(self.user.email, new_email)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertIn(new_email, User._registered_emails)

    def test_get_by_id(self):
        retrieved_user = User.get_by_id(self.user.id)
        self.assertEqual(retrieved_user, self.user)

    def test_get_by_email(self):
        retrieved_user = User.get_by_email(self.user.email)
        self.assertEqual(retrieved_user, self.user)

    def test_delete_user(self):
        user_id = self.user.id
        User.delete_user(user_id)
        self.assertNotIn(self.user, User.users)
        self.assertNotIn(self.user.email, User._registered_emails)

if __name__ == "__main__":
    unittest.main()