#!/usr/bin/python3
"""Module test_state"""
import unittest
from models.base_model import BaseModel
from models.state import State



class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up test fixtures"""
        self.state = State()

    def test_attributes(self):
        """Test that the State instance has the required attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_str(self):
        """Test that the __str__ method returns a string"""
        bm1 = BaseModel()
        str_output = str(bm1)
        self.assertIn(f"[BaseModel] ({bm1.id})", str_output)
        self.assertIn("'id':", str_output)
        self.assertIn("'created_at':", str_output)
        self.assertIn("'updated_at':", str_output)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertTrue("id" in state_dict)
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("__class__" in state_dict)

    def test_init_kwargs(self):
        """Test that the State instance is correctly created using kwargs"""
        kwargs = {"name": "California"}
        state = State(**kwargs)
        self.assertEqual(state.name, kwargs["name"])

    def tearDown(self):
        """Tear down test fixtures"""
        from models import storage
        storage.delete(self.state)
        
if __name__ == '__main__':
    unittest.main()
