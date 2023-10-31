#!/usr/bin/python3
"""AirBnB clone"""
from . import storage
from datetime import datetime
import uuid


class BaseModel():
    """Defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """BaseModel class constructor"""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            ISO_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(kwargs['created_at'], ISO_fmt)
            self.updated_at = datetime.strptime(kwargs['updated_at'], ISO_fmt)
            for key, value in kwargs.items():
                if key not in ('created_at', 'updated_at', '__class__'):
                    self.__dict__[key] = value

    def __str__(self):
        """Returns the string representation of BaseModel"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
