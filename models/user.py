#!usr/bin/python3
"""The `User` module

It defines one class, `User(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
