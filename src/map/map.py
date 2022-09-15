from src.display.camera import Camera
from src.map.room import Room


class Map:
    
    TMP = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    
    @classmethod
    def init(cls):
        cls.rooms = [
            Room(),
        ]
    
    @classmethod
    def generate_level(cls, player):
        Camera.empty()
        
        for y, row in enumerate(cls.TMP):
            for x, room_id in enumerate(row):
                cls.rooms[room_id].place(x, y)
                
        Camera.add(player)
        