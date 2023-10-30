#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({key: obj.to_dict() for key, obj in
                       FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {key: self.__models()
                                         [value["__class__"]](**value)
                                         for key, value in json.load(f).items()
                                         }
        except FileNotFoundError:
            pass