#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Base Model Module

This module is in charge of establishing a reference
Base Model for the rest of the classes of the
HBNB project (Airbnb Clone), from which it will be possible
to extract information such as: A unique universal identifier,
the date and time in which a class was created and updated,
a standard format to print the class content, a way to save
the data created from the instances and finally the representation
of all the keys and values of an instance.

"""

from datetime import datetime
import uuid


class BaseModel:
    """Base Model Class

    This is the Base Model that take care of the
    initialization, serialization and deserialization
    of the future instances.

    Attributes:
        id (str): It's an UUID for when an instance is created.
        created_at (datetime): The current date and time that
            an instance is created.
        updated_at (datetime): The current date and time that
            an instance is created and it will be updated every
            time that the object changes.

    """

    def __init__(self):
        """Base Model __init__ Method

        Here, the default values of a Base Model
        instance are initialized.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Another documentation

        Any documentation

        """
        return '[{0}] ({1})'.format(self.__class__.__name__, self.id)
