import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Testing File Storage functionality """

    def setUp(self):
        self.fs = FileStorage()

    def tearDown(self):
        """ Clean up after tests """
        for obj in list(self.fs.all().values()):
            self.fs.delete(obj)

    def test_all(self):
        """Test all"""
        fs2 = FileStorage()
        self.assertEqual(self.fs.all(), fs2.all())

    def test_new(self):
        """Test new"""
        bm1 = BaseModel()
        self.fs.new(bm1)
        self.assertIn(f'BaseModel.{bm1.id}', self.fs.all()) # Check if object is added

    def test_save(self):
        """Test save"""
        bm2 = BaseModel()
        self.fs.new(bm2) # Add object to storage
        self.fs.save() # Save the object
        with open('file.json', 'r') as f:
            self.assertIn(f'BaseModel.{bm2.id}', f.read()) # Check if object is saved

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