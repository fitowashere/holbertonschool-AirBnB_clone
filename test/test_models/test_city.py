#!/usr/bin/python3
"""Module test_city"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City Functionality"""

    def setUp(self):
        """Set up"""
        self.city = City()

    def tearDown(self):
        """Clean up after testing."""
        del self.city
        
    def test_name(self):
        """Test name"""
        self.assertEqual(self.city.name, '')

    def test_state_id(self):
        """Test state_id"""
        self.assertEqual(self.city.state_id, '')

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'id'))

    def test_attribute_defaults(self):
        """Test attribute"""
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')

    def test_str(self):
        """Test STR"""
        bm1 = BaseModel()
        str_output = str(bm1)
        self.assertIn(f"[BaseModel] ({bm1.id})", str_output)
        self.assertIn("'id':", str_output)
        self.assertIn("'created_at':", str_output)
        self.assertIn("'updated_at':", str_output)

if __name__ == '__main__':
    unittest.main()
