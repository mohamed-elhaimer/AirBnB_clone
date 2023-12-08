from  models.base_model import BaseModel
from models.engine.file_storage import FileStorage

test = FileStorage()
data = {'id': 'bd9146e3-a0fe-46dd-b249-340a665d523f', 'created_at': '2023-12-06T18:19:40.362558', 'updated_at': '2023-12-06T18:19:40.362558', 'name': 'XXXX', '__class__': 'BaseModel'}
obj = BaseModel(**data)
print("--------")
print(test.new(obj))
