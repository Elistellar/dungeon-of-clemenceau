from pygame.math import Vector2

from src.display.camera import Camera
from src.display.resource import Resource
from src.world.tmx.tile import Tile
from src.actors.player import Player


class Level:
    
    def __init__(self, n: int, player: Player):
        Camera.empty()
        
        # All here is temporary, just for developpement
        room = Resource.tmx("1")
        
        floor = Tile(Vector2(), room.floor.surface)
        Camera.background.add(floor)

        Camera.add(room.relief.tiles)

        Camera.add(player)
