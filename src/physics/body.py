from pygame import Rect
from pygame import Vector2

from src.utils.consts import TILE_SIZE

class Body:
    """
    Object with a hitbox that can collide with others
    """

    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    # to overwite
    SPRITE_SHEET_NAME: str
    
    HITBOX = 0, 0

    def __init__(self, pos):
        self.pos = pos + self.CENTER_POS
        self.rect = Rect(*self.pos, TILE_SIZE, TILE_SIZE)
        self.hitbox = self.rect.inflate(self.HITBOX)