#!/usr/bin/python3
"""Module test_place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up test fixtures"""
        self.place = Place()

    def tearDown(self):
        """Tear down test fixtures"""
        storage.delete(self.place)
        
    def test_instantiation(self):
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertIsInstance(p, BaseModel)

    def test_attributes(self):
        """Test that the Place instance has the required attributes"""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

    def test_str(self):
        """Test that the __str__ method returns a string"""
        p = Place()
        str_output = str(p)
        self.assertIn(f"[Place] ({p.id})", str_output)
        self.assertIn("'id':", str_output)
        self.assertIn("'created_at':", str_output)
        self.assertIn("'updated_at':", str_output)

    def test_to_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        p.name = "My Place"
        p.city_id = "123"
        d = p.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["name"], "My Place")
        self.assertEqual(d["city_id"], "123")
        self.assertEqual(d["__class__"], "Place")

if __name__ == '__main__':
    unittest.main()
