import os
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)
    def reload(self):
        current_classes = {'BaseModel': BaseModel, 'User': User}
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None
            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass
            if deserialized is None:
                return
            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}