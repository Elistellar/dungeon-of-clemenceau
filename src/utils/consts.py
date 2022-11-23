from enum import Enum


FRAMERATE = 60

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
COLOR_CURSOR = (80, 80, 80)

COLOR_BLACK = (0, 0, 0)
COLOR_BLACK_ALPHA = (0, 0, 0, 0)