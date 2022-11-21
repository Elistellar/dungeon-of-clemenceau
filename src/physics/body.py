from pygame import Rect
from pygame.math import Vector2

from src.utils.consts import TILE_SIZE


class Body:
    """
    Object with a hitbox that can collide with others
    """

    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    # to overwite
    SPRITE_SHEET_NAME: str
    
    HITBOX = 0, 0

    def __init__(self, rect: Rect):
        self.pos = rect.center + self.CENTER_POS
        self.rect = rect
        self.hitbox = self.rect.inflate(self.HITBOX)
