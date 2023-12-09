#!/usr/bin/python3
import uuid
from datetime import datetime
import models
class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().date()
            self.updated_at = datetime.now().date()
        models.storage.new(self)
    def __str__(self):
        return ("[" + str(self.__class__.__name__) + "] " + "(" + str(self.id) + ") " + str(self.__dict__))
    def save(self):
        self.updated_at = datetime.now().date()
        models.storage.save()
    def to_dict(self):
        my_dic = self.__dict__
        my_dic['__class__'] = self.__class__.__name__
        my_dic['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        my_dic['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return (my_dic)