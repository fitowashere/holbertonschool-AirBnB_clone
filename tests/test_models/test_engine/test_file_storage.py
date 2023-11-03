#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    """ Testing File Storae functionality """

    def setUp(self):
        self.fs = FileStorage()
        self.file_path = 'file.json'

    def tearDown(self):
        """Tear down"""
        os.remove(self.file_path)

    def test_all(self):
        """Test all"""
        fs2 = FileStorage()
        self.assertEqual(self.fs.all(), fs2.all())

    def test_new(self):
        """Test new"""
        bm1 = BaseModel()
        self.assertEqual(len(self.fs.all()), 0)  # Empty
        self.fs.new(bm1)
        self.assertEqual(len(self.fs.all()), 1)  # 1 object stored
        self.assertIn(f'BaseModel.{bm1.id}', self.fs.all())

    def test_save(self):
        """Test save"""
        bm1 = BaseModel()
        self.assertEqual(len(self.fs.all()), 0) # Empty
        self.fs.new(bm1)
        self.assertEqual(len(self.fs.all()), 1) # 1 object stored
        self.assertIn(f'BaseModel.{bm1.id}', self.fs.all())

        self.fs.save()
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1) # 1 object stored
            self.assertIn(f'BaseModel.{bm1.id}', data)

    def test_delete(self):
        """Test delete method of FileStorage"""
        bm = BaseModel()
        self.fs.new(bm)  # Adding the object to the storage
        self.assertIn(f"BaseModel.{bm.id}", self.fs.all())  # Check if object is added

        # Now delete the object and check if it's removed
        self.fs.delete(bm)
        self.assertNotIn(f"BaseModel.{bm.id}", self.fs.all())  # Object should be removed

if __name__ == '__main__':
    unittest.main()