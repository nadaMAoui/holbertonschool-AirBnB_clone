import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(dictionary, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                dictionary = json.load(f)
            for key, value in dictionary.items():
                obj = eval(value['__class__'])(**value)
                self.new(obj)
        except:
            pass
