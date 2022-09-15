from pygame import Rect

from src.display.resources_loader import ResourcesLoader
from src.map.tile import Tile


class Layer:
    
    SIZE = 16
    
    def __init__(self, data: list[list[int]]):
        self.data = data
        
    def place(self, x, y):
        for _y, row in enumerate(self.data):
            for _x, tile_id in enumerate(row):
                Tile(
                    ResourcesLoader.tile_surfaces[tile_id],
                    Rect(
                        (x * self.SIZE + _x) * ResourcesLoader.TILE_SIZE,
                        (y * self.SIZE + _y) * ResourcesLoader.TILE_SIZE,
                        ResourcesLoader.TILE_SIZE,
                        ResourcesLoader.TILE_SIZE
                    )
                )
