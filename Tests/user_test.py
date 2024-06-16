import unittest
from datetime import datetime
from uuid import uuid4
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        User._registered_emails.clear()
        User.users.clear()
        self.user = User("John", "Doe", "john.doe@example.com", "password123")

    def tearDown(self):
        User._registered_emails.clear()
        User.users.clear()

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertTrue(self.user.check_password("password123"))
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(len(self.user.reviews), 0)
        self.assertEqual(len(self.user.places), 0)

    def test_duplicate_email(self):
        with self.assertRaises(ValueError):
            duplicate_user = User("Jane", "Doe", "john.doe@example.com", "differentpassword")

    def test_change_password(self):
        self.user.change_password("newpassword")
        self.assertTrue(self.user.check_password("newpassword"))

    def test_add_review(self):
        review = "Great place!"
        self.user.add_review(review)
        self.assertIn(review, self.user.reviews)

    def test_remove_review(self):
        review = "Bad experience!"
        self.user.add_review(review)
        self.user.remove_review(review)
        self.assertNotIn(review, self.user.reviews)

    def test_add_place(self):
        place = "Beautiful beach"
        self.user.add_place(place)
        self.assertIn(place, self.user.places)

    def test_remove_place(self):
        place = "Old house"
        self.user.add_place(place)
        self.user.remove_place(place)
        self.assertNotIn(place, self.user.places)

    def test_update_email(self):
        new_email = "john.doe.new@example.com"
        self.user.update(email=new_email)
        self.assertEqual(self.user.email, new_email)
        self.assertIn(new_email, User._registered_emails)
        self.assertNotIn("john.doe@example.com", User._registered_emails)

    def test_get_by_id(self):
        retrieved_user = User.get_by_id(self.user.id)
        self.assertEqual(retrieved_user, self.user)

    def test_get_by_email(self):
        retrieved_user = User.get_by_email(self.user.email)
        self.assertEqual(retrieved_user, self.user)

    def test_delete_user(self):
        User.delete_user(self.user.id)
        self.assertNotIn(self.user, User.users)
        self.assertNotIn(self.user.email, User._registered_emails)


if __name__ == '__main__':
    unittest.main()
