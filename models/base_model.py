import uuid
"""import uuid module"""
from datetime import datetime  
class BaseModel:
    """base class"""
    def __init__(self, *args, **kwargs):
        input_format = "%Y-%m-%dT%H:%M:%S.%f"
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(value, input_format)
            setattr(self, key, value)
    def __str__(self):
        return ("[" + str(self.__class__.__name__) + "] " + "(" + str(self.id) + ") " + str(self.__dict__))
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        """the dictionary return"""
        my_dic = self.__dict__
        my_dic ["__class__"] = self.__class__.__name__
        my_dic ["created_at"] = self.created_at.isoformat()
        my_dic ["updated_at"] = self.updated_at.isoformat()
        return my_dic
