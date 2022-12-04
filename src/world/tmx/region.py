from xml.etree.ElementTree import Element as XMLElement
from typing import Callable
from pathlib import Path

from pygame import Rect

from src.utils.consts import ROOM_SIZE, TILE_SIZE
from src.world.tmx.layer import Layer
from src.world.tmx.tileset import Tileset
from src.world.obstacles import Obstacle


class Region:
    """
    Represent a tmx map.
    """
    
    def __init__(self, root: XMLElement, file_location: Path, get_tileset: Callable[[Path], Tileset]):
        """
        Load the given tmx map.
        
        Raises:
            - ValueError if the file does not fit to the requiered properties
        """
        
        # Integrity check
        attribs = root.attrib
        if attribs.get("orientation") != "orthogonal" \
        or attribs.get("infinite")    != "0" \
        or attribs.get("tilewidth")   != str(TILE_SIZE) \
        or attribs.get("tileheight")  != str(TILE_SIZE) \
        or attribs.get("width")       != str(ROOM_SIZE) \
        or attribs.get("height")      != str(ROOM_SIZE):
            raise ValueError()
        
        # Load tileset
        tileset_path = root.find("tileset").attrib["source"]        
        tileset = get_tileset(file_location / tileset_path)
        
        # Load layers
        for layer_element in root.findall("layer"):
            if layer_element.attrib["name"] == "floor":
                self.floor = Layer(layer_element, tileset, True)
                
            elif layer_element.attrib["name"] == "relief":
                self.relief = Layer(layer_element, tileset)
                
        # Load object groups
        self.obstacles = []
        for object_group_element in root.findall("objectgroup"):
            
            if object_group_element.attrib["name"] == "wall":
                for object_element in object_group_element.findall("object"):
                    self.obstacles.append(                        
                        Obstacle(Rect(
                            float(object_element.attrib["x"]),
                            float(object_element.attrib["y"]),
                            float(object_element.attrib["width"]),
                            float(object_element.attrib["height"])
                        ))
                    )
