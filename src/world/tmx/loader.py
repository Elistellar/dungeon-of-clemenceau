from src.utils.path import path
from src.world.tmx.map import Map


class TmxLoader:
    
    ROOM_DIR = "assets/map/rooms/"
    room_paths = [
        "1.tmx",
    ]
    
    rooms = []
    
    @classmethod
    def load(cls):
        for fpath in cls.room_paths:
            try:
                cls.rooms.append(
                    Map(path(cls.ROOM_DIR + fpath))
                )
            except:
                raise ValueError(f"Corrupted file : {fpath}")
