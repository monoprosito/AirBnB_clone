#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""User Module
This Module inherits from BaseModel class.
User Module contains the attributes to be assigned
to the Users.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class
    This is the User Class ...
    Attributes:
        ...
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
