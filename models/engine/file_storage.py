#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj
    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k:v.to_dict() for k, v in self.__objects.items()}, f)
    def reload(self):
        current_class = {"BaseModel" : BaseModel}
        if not os.path.exists(self.__file_path):
            return
        else:
            with open(self.__file_path, 'r') as f:
                deserialized = None
                try:
                    deserialized = json.load(f)
                except json.JSONDecodeError:
                    pass
                if deserialized is None:
                    return
                self.__objects =  {
                k: current_class[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
