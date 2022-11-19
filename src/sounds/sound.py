from src.display.resource_loader import ResourceLoader
from src.settings.settings import Settings


class Sound:
    """
    Handle all sounds.
    """
    
    channels = {
        "entity": 50, 
        "menu": 50,
        "music": 50,
    }
    
    @classmethod
    def load(cls):
        for name in cls.channels.keys():
            cls.set_channel_volume(name, Settings[f"volume.{name}"])
    
    @classmethod
    def set_channel_volume(cls, channel_name: str, volume: int):
        """
        volume is an int between 0 and 100 
        """
        cls.channels[channel_name] = volume / 100
        
    @classmethod
    def play(cls, sound_name: str, channel_name: str):
        s = ResourceLoader[f"sound.{sound_name}"]
        s.set_volume(cls.channels[channel_name])
        s.play()
    