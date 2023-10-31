#!/usr/bin/python3
""" Storage engine for AirBnB clone """
import json
from os import path


class FileStorage():
    """Class meant to manage JSON file storage"""
    __file_path = 'HBnB_objects.json'
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets a new object as value in __objects with key"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_dict = dict()
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file"""
        from ..base_model import BaseModel


        classes = [BaseModel]
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