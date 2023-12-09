import uuid
import models

"""import uuid module"""
from datetime import datetime
class BaseModel:
    """base class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            input_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)
    def __str__(self):
        return ("[" + str(self.__class__.__name__) + "] " + "(" + str(self.id) + ") " + str(self.__dict__))
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """the dictionary return"""
        dict = self.__dict__
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict
