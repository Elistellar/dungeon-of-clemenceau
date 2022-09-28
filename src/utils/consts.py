from enum import Enum


TILE_SIZE = 32
ROOM_SIZE = 16

class Orientation(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST  = "east"
    WEST  = "west"


COLOR_BTN_TEXT = (255, 255, 255)
COLOR_BTN_BG = (150, 150, 150)
COLOR_BTN_BG_HOVER = (200, 200, 200)
