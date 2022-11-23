from pygame.math import Vector2

from src.actors.entity import Entity
from src.commanding.player_node import PlayerNode


class Player(Entity):
    """
    The player sprite
    """
    
    SPRITE_SHEET_NAME = "balan_tmp"
    HITBOX = -14, -20
    
    class speeds:
        WALK = 0.2
        SPRINT = 0.4
    
    def __init__(self, pos: Vector2):
        super().__init__(pos)

        self.brain = PlayerNode()
        
        self.paused = False

    def update(self, dt: int):
        
        if not self.paused:

            # performs standard entity actions
            super().update(dt)
