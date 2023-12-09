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
        return self.__objects
    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            data = {k:v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, f)
    def reload(self):
        current_class = {"BaseModel" : BaseModel}
        if not os.path.exists(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, 'r') as f:
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
