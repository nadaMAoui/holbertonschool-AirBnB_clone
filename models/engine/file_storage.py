#!/usr/bin/python3
"""
Filestorage funtion all, new, save, reload, delete, get
"""
from models.user import User
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            result = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    result[key] = value
            return result

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            file.write(json.dumps(new_dict))

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == "User":
                        obj = User(**value)
                    else:
                        obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            del self.__objects[key]

    def get(self, cls, id):
        key = cls.__name__ + '.' + id
        return self.__objects.get(key, None)
