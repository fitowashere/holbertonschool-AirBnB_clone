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
        self.assertEqual(str(self.state), "[State] ({}) {}".format(
            self.state.id, self.state.__dict__))

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

if __name__ == '__main__':
    unittest.main()
