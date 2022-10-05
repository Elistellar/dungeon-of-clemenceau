from csv import reader as csv_reader
from xml.etree.ElementTree import Element as XMLElement

from pygame import Surface, Vector2
from pygame.locals import SRCALPHA

from src.utils.consts import ROOM_SIZE, TILE_SIZE
from src.world.tmx.tileset import Tileset
from src.world.tmx.tile import Tile


class Layer:
    """
    Represent a tmx layer.
    """
    
    def __init__(self, xml: XMLElement, tileset: Tileset, single_image = False):
        """
        Parameters:
            xml (XMLElement): the layer data.
            tileset (Tileset): the tileset object.
            single_image (bool): if True, load all tileset as a single image. Else, each tile will be load as a Sprite.
        """
        
        if xml.attrib.get("width")  != str(ROOM_SIZE) \
        or xml.attrib.get("height") != str(ROOM_SIZE):
            raise AttributeError()
        
        if single_image:
            self.surface = Surface((TILE_SIZE * ROOM_SIZE, TILE_SIZE * ROOM_SIZE), SRCALPHA)
        else:
            self.tiles = []
            
        raw_data = xml.find("data").text
        csv_data = csv_reader(raw_data.splitlines())
       
        csv_data.__next__()
        for y, row in enumerate(csv_data):
            for x, i in enumerate(row):
                if not i: continue
                
                i = int(i)
                
                if single_image:                    
                    self.surface.blit(
                        tileset[i],
                        (
                            x * TILE_SIZE,
                            y * TILE_SIZE,
                        )
                    )
                elif i:
                    self.tiles.append(
                        Tile(Vector2(x, y) * TILE_SIZE, tileset[i])
                    )
