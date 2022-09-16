from xml.etree.ElementTree import parse as XMLparse

from src.utils.consts import TILE_SIZE, ROOM_SIZE
from src.world.tmx.layer import Layer
from src.world.tmx.tileset import Tileset


class Map:
    
    def __init__(cls, file_path):
        tree = XMLparse(file_path)
        root = tree.getroot()
        
        # Integrity check
        attribs = root.attrib
        if attribs.get("orientation") != "orthogonal" \
        or attribs.get("infinite")    != "0" \
        or attribs.get("tilewidth")   != str(TILE_SIZE) \
        or attribs.get("tileheight")  != str(TILE_SIZE) \
        or attribs.get("width")       != str(ROOM_SIZE) \
        or attribs.get("height")      != str(ROOM_SIZE):
            raise AttributeError(f"Corrupted file {file_path}")
        
        # Load tileset
        tileset_path = root.find("tileset").attrib["source"]
        tileset = Tileset.load(file_path, tileset_path)
        
        # Load layers
        for layer_element in root.findall("layer"):
            if layer_element.attrib["name"] == "floor":
                cls.floor = Layer(layer_element, tileset, True)
