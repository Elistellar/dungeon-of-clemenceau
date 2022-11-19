from json import dump as json_dump
from json import load as json_load
from typing import Any

from src.utils.path import path


class Settings:
    """
    Handle all settings.
    """
    
    @classmethod
    def load(cls):
        with open(path("src/settings/config.json"), encoding="utf-8") as file:
            cls.data = json_load(file)
            
    def __class_getitem__(cls, key: str):
        return cls.data[key]
    
    @classmethod
    def set(cls, key: str, value: Any) -> Any:
        """
        Save the given setting and returns it.
        """
        cls.data[key] = value
        
        with open(path("src/settings/config.json"), "w", encoding="utf-8") as file:
            json_dump(cls.data, file, indent=4)
            
        return value
