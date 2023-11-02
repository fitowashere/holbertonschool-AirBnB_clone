#!/usr/bin/python3
"""Module test_file_storage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User

class TestFileStorage(unittest.TestCase):
    """ Testing File Storage functionality """

    def setUp(self):
        """Set up: Reset storage and ensure starting with a clean state."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Reset FileStorage and delete the file.json after each test"""
        FileStorage._FileStorage__objects = {}  # Reset internal objects dictionary
        if os.path.exists("file.json"):
            os.remove("file.json")  # Ensure the file.json is deleted

    def test_all(self):
        """Test all method of FileStorage."""
        bm = BaseModel()
        storage.new(bm)
        self.assertIn(f'BaseModel.{bm.id}', storage.all())  # Check if the new object is in storage

    def test_new(self):
        """Test new"""
        obj3 = City()
        storage.new(obj3)
        objs = storage.all()
        self.assertIn(f"{type(obj3).__name__}.{obj3.id}", objs)

    def test_save(self):
        """Test save method of FileStorage."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        self.assertTrue(os.path.isfile('file.json'))  # Check if file.json is created

        with open('file.json', 'r') as f:
            data = json.load(f)
        self.assertIn(f'BaseModel.{bm.id}', data)  # Check if the BaseModel object is saved
    
    def test_reload(self):
        """Test reload method of FileStorage."""
        # Ensure initial state is clean
        self.assertEqual(len(storage.all()), 0, "Initial storage is not empty")

        # Create a new BaseModel object, save it, and then clear the storage
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        object_id = f'BaseModel.{bm.id}'
        self.assertIn(object_id, storage.all())

        # Clearing the objects and ensuring storage is empty before reload
        FileStorage._FileStorage__objects = {}
        self.assertEqual(len(storage.all()), 0, "Storage not cleared before reload")

        # Reload and check if the object is restored
        storage.reload()
        self.assertIn(object_id, storage.all(), "Object not found after reload")


if __name__ == '__main__':
    unittest.main()
