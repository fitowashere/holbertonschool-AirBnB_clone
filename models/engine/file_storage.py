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
        from ..base_model import BaseModel


        classes = [BaseModel, User]
        class_dict = dict()
        for c in classes:
            class_dict[c.__name__] = c

        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content is not None and content != '':
                    json_dict = json.loads(content)
                    for key, value in json_dict.items():
                        obj_class = class_dict[value['__class__']]
                        self.__objects[key] = obj_class(**value)
        else:
            pass
