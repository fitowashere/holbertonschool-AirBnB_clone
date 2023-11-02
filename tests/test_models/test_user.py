#!/usr/bin/python3
"""Module test_user"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test fixtures"""
        self.user = User()
        self.user2 = User()
        self.user2.email = "user@example.com"
        self.user2.password = "password"
        self.user2.first_name = "Betty"
        self.user2.last_name = "Kernel"
        self.user2.save()


    def test_attributes(self):
        """Test that the User instance has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_str(self):
        """Test that the __str__ method returns a string"""
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue("id" in user_dict)
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)
        self.assertTrue("__class__" in user_dict)

    def test_init_kwargs(self):
        """Test that the User instance is correctly created using kwargs"""
        kwargs = {"email": "test@test.com", "password": "password",
                  "first_name": "John", "last_name": "Doe"}
        user = User(**kwargs)
        self.assertEqual(user.email, kwargs["email"])
        self.assertEqual(user.password, kwargs["password"])
        self.assertEqual(user.first_name, kwargs["first_name"])
        self.assertEqual(user.last_name, kwargs["last_name"])

    def test_init_args(self):
        """Test that the User instance is correctly created using keyword arguments"""
        kwargs = {
            "email": "test@test.com",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe"
        }
        user = User(**kwargs)
        self.assertEqual(user.email, kwargs['email'])
        self.assertEqual(user.password, kwargs['password'])
        self.assertEqual(user.first_name, kwargs['first_name'])
        self.assertEqual(user.last_name, kwargs['last_name'])
        def test_init_no_args(self):
            """Test that the User instance is correctly created without args"""
            user = User()
            self.assertEqual(user.email, "")
            self.assertEqual(user.password, "")
            self.assertEqual(user.first_name, "")
            self.assertEqual(user.last_name, "")

    def tearDown(self):
        """Tear down test fixtures"""
        del self.user
        del self.user2
        storage.delete()
        storage.save()

if __name__ == '__main__':
    unittest.main()
