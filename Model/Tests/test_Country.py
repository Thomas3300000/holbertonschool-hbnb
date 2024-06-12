import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app # type: ignore

class TestCountryEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    def test_get_country_by_code(self):
        response = self.app.get('/countries/FR')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'France')

    def test_get_nonexistent_country(self):
        response = self.app.get('/countries/XX')
        self.assertEqual(response.status_code, 404)

    def test_get_cities_by_country(self):
        self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        response = self.app.get('/countries/FR/cities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_cities_nonexistent_country(self):
        response = self.app.get('/countries/XX/cities')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
