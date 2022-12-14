from xml.etree.ElementTree import parse as XMLparse
from pathlib import Path

from pygame import Surface
from pygame.image import load as load_image
from pygame.locals import SRCALPHA

from src.utils.consts import TILE_SIZE


class Tileset:
    """
    Represent a tmx tileset
    """
    
    def __init__(self, file_path: Path):
        tree = XMLparse(file_path)
        root = tree.getroot()
        image_path = file_path.parent / root.find("image").attrib["source"]
        surface = load_image(image_path).convert_alpha()
        
        self.tiles = [
            Surface((TILE_SIZE, TILE_SIZE), SRCALPHA),
        ]
        
        for y in range(0, surface.get_height(), TILE_SIZE):
            for x in range(0, surface.get_width(), TILE_SIZE):
                
                s = Surface((TILE_SIZE, TILE_SIZE), SRCALPHA)
                s.blit(
                    surface,
                    (0, 0),
                    (x, y, TILE_SIZE, TILE_SIZE)
                )
                self.tiles.append(s)

    def __getitem__(self, key: int) -> Surface:
        return self.tiles[key]
