import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.City import City

class TestCityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        City._cities = []

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

    def test_create_city(self):
        response = self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "Paris")
        self.assertEqual(response.json['country_code'], "FR")

    def test_create_duplicate_city(self):
        self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        response = self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        self.assertEqual(response.status_code, 409)

    def test_create_city_invalid_country(self):
        response = self.app.post('/cities', json={"name": "Paris", "country_code": "XX"})
        self.assertEqual(response.status_code, 400)

    def test_get_all_cities(self):
        self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_city_by_id(self):
        city_response = self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        city_id = city_response.json['id']
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Paris")

    def test_get_nonexistent_city(self):
        response = self.app.get('/cities/invalid-id')
        self.assertEqual(response.status_code, 404)

    def test_update_city(self):
        city_response = self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        city_id = city_response.json['id']
        response = self.app.put(f'/cities/{city_id}', json={"name": "New Paris"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "New Paris")

    def test_update_city_duplicate_name(self):
        self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        city_response = self.app.post('/cities', json={"name": "Lyon", "country_code": "FR"})
        city_id = city_response.json['id']
        response = self.app.put(f'/cities/{city_id}', json={"name": "Paris"})
        self.assertEqual(response.status_code, 409)

    def test_delete_city(self):
        city_response = self.app.post('/cities', json={"name": "Paris", "country_code": "FR"})
        city_id = city_response.json['id']
        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
