#!/usr/bin/python3
"""
Filestorage funtion all, new, save, reload, delete, get
"""

from models.base_model import BaseModel
from models.user import User

class FileStorage:
    ...
    
    def _objects_from_file(self):
        ...
        
        for key, value in self.__objects.items():
            class_name = key.split(".")[0]
            if class_name == "BaseModel":
                obj = BaseModel(**value)
            elif class_name == "User":
                obj = User(**value)
            else:
                continue
            self.new(obj)
