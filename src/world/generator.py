from pygame import Vector2

from src.display.camera import Camera
from src.world.tmx.loader import TmxLoader
from src.world.tmx.tile import Tile

class LevelGenerator:
    
    @classmethod
    def generate(cls, player):
        Camera.empty()
        
        room = TmxLoader.rooms[0]
        
        floor = Tile(Vector2(), room.floor.surface)
        Camera.background.add(floor)
                
        Camera.add(player)
