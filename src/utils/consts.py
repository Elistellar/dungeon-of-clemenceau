from enum import Enum


TILE_SIZE = 32
ROOM_SIZE = 16

class Orientation(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST  = "east"
    WEST  = "west"
