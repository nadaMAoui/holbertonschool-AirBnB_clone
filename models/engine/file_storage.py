#!/usr/bin/python3
"""FileStorage is responsible for managing the serialization/deserialization
of BaseModel instances to/from a JSON file
"""

import json
import os.path


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                objects_dict = json.load(f)
            for key, value in objects_dict.items():
                class_name, obj_id = key.split('.')
                value['__class__'] = class_name
                self.__objects[key] = eval(class_name)(**value)
