#!/usr/bin/python3
import uuid
import datetime
"""Base model module"""


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialises the BaseModel class"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return the string representation of instance"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        updated_at = datetime.datetime.now()

    def to_dict(self):
        class_dict = self.__dict__
        class_dict['__class__'] = type(self).__name__
        class_dict['created_at'] = class_dict['created_at'].isoformat(timespec='microseconds')
        class_dict['updated_at'] = class_dict['updated_at'].isoformat(timespec='microseconds')
        return class_dict
