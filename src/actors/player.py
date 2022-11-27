from pygame.math import Vector2

from src.actors.creature import Creature
from src.commanding.player_node import PlayerNode


class Player(Creature):
    """
    The player sprite
    """
    
    SPRITE_SHEET_NAME = "balan_tmp"
    HITBOX = -14, -20
    
    
    def __init__(self, pos: Vector2):
        super().__init__(pos, 100)

        self.brain = PlayerNode()
        
        self.paused = False

    def update(self, dt: int):
        
        if not self.paused:

            # performs standard entity actions
            super().update(dt)
