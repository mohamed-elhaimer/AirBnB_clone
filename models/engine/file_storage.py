import json
import os
from ..base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        data = obj.BaseModel.to_dict()
        self.__objects[key] = data
        return self.__objects
    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)
    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        else:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)


