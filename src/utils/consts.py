from enum import Enum


FRAMERATE = 60

TILE_SIZE = 32
ROOM_SIZE = 16

class Orientation(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST  = "east"
    WEST  = "west"

CONSTRAIN_DECREASE = 0.1
PROJECTILE_BASE_HEIGHT = 40

JOY_A = 0
JOY_B = 1
JOY_X = 2
JOY_Y = 3
JOY_SELECT = 6
JOY_START = 7

COLOR_BLACK = (0, 0, 0)
COLOR_BLACK_ALPHA = (0, 0, 0, 0)
COLOR_BUTTON_TEXT = (200, 200, 200)
COLOR_MENU_BACKGROUND = (0, 0, 0, 192)
