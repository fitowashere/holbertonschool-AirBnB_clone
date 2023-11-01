#!/usr/bin/python3
"""Base Model"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """BaseModel class constructor. `*args` can be used for future positional arguments."""
        if kwargs:
            # Set each key in kwargs, with special handling for dates and ID.
            self.id = kwargs.get('id', str(uuid.uuid4()))
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key in ['created_at', 'updated_at']:
                value = kwargs.get(key)
                if value:
                    try:
                        setattr(self, key, datetime.strptime(value, date_format))
                    except ValueError:
                        setattr(self, key, datetime.now())
                else:
                    setattr(self, key, datetime.now())

            for key, value in kwargs.items():
                if key not in ('id', 'created_at', 'updated_at', '__class__'):
                    setattr(self, key, value)
        else:
            # If kwargs is empty, assign default values
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Method that returns a string representation of the BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
 
    def save(self):
        """
        Method that updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
