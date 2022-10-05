from enum import Enum
from json import load as json_load

from src.settings import Settings
from src.utils.path import path


class Lang:
    """
    Handle all texts.
    """
    
    class Langs(Enum):
        FR = "fr"
        EN = "en"
    
    @classmethod
    def load(cls, lang: Langs):
        with open(path("assets/lang/" + lang.value + ".json"), encoding="utf-8") as file:
            cls.data = json_load(file)
            
        Settings.set("lang", lang.value)
            
    def __class_getitem__(cls, key: str) -> str:
        """
        Returns the text associated to the given code.
        """
        return cls.data.get(key, key)
        