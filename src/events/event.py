from enum import Enum


class Event:
    
    def __init__(self, _type: int, **kwargs):
        self.type = _type
        for key, value in kwargs.items():
            setattr(self, key, value)
