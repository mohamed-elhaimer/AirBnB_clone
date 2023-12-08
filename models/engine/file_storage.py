#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in  FileStorage.__objects.items()}, f)
    def reload(self):
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            json.load(f)
