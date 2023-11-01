#!/usr/bin/python3
""" Storage engine for AirBnB clone """
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """Class meant to manage JSON file storage"""
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file"""
        from models.base_model import BaseModel

        classes = [BaseModel, User]
        class_dict = {c.__name__: c for c in classes}

        try:
            if path.exists(self.__file_path):
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content:
                        json_dict = json.loads(content)
                        for key, value in json_dict.items():
                            obj_class = class_dict.get(value['__class__'])
                            if obj_class:
                                self.__objects[key] = obj_class(**value)
        except Exception as e:
            # Handle exceptions
            print(f"Error while reloading JSON file: {e}")

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()