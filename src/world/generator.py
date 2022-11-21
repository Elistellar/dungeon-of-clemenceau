from typing import TYPE_CHECKING

from pygame import Vector2

from src.display.camera import Camera
from src.world.tmx.loader import TmxLoader
from src.world.tmx.tile import Tile
from src.data_storing.data_storage import DataStorage

if TYPE_CHECKING:
    from src.actors.player import Player


class LevelGenerator:
    
    @classmethod
    def generate(cls, player: "Player"):
        """
        Clear the current level and generate another one.
        """
        Camera.empty()
        DataStorage.obstacles.empty()
        
        room = TmxLoader.rooms[0]
        
        floor = Tile(Vector2(), room.floor.surface)
        Camera.background.add(floor)
        DataStorage.obstacles.add(room.obstacles)
        
        Camera.add(room.relief.tiles)
        DataStorage.obstacles.add(room.obstacles)
        
        Camera.add(player)
