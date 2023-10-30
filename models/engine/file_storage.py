#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json


class FileStorage:
    """Serializes instances to a JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
