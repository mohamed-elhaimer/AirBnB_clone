from models import storage
from models.base_model import BaseModel



print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model)
my_model.save()