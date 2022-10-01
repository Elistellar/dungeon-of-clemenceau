from enum import Enum

WINDOW_SIZE = 1280, 720

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
