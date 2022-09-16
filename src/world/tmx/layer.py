from csv import reader as csv_reader
from xml.etree.ElementTree import Element as XMLElement

from pygame import Surface
from pygame.locals import SRCALPHA

from src.utils.consts import ROOM_SIZE, TILE_SIZE
from src.world.tmx.tileset import Tileset


class Layer:
    
    def __init__(self, xml: XMLElement, tileset: Tileset, single_image = False):
        
        if xml.attrib.get("width")  != str(ROOM_SIZE) \
        or xml.attrib.get("height") != str(ROOM_SIZE):
            raise AttributeError()
        
        if single_image:
            self.surface = Surface((TILE_SIZE * ROOM_SIZE, TILE_SIZE * ROOM_SIZE), SRCALPHA)
        
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
