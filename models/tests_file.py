#!/usr/bin/python3
import unittest
import uuid
from entities_classes import User


"""..."""


class TestUser(unittest.TestCase):
    """..."""
    def test_user_creation(self):
        """..."""
        user = User(uuid, "example@example.com", "1234", "Betty", "Holberton")
        self.assertEqual(user.email, "example@example.com")
        self.assertEqual(user.first_name, "Betty")
        self.assertEqual(user.last_name, "Holberton")
        self.assertIsNotNone(user.user_id)


if __name__ == "__main__":
    unittest.main()
