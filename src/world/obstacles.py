from pygame.math import Vector2
from pygame.sprite import Sprite
from src.physics.body import Body


class Obstacle(Sprite):
    """
    A sprite that only have an hitbox.
    """
    
    def __init__(self, pos: Vector2):
        """
        Create a new obstacle.
        """
        Sprite.__init__(self)
        Body.__init__(self, pos)
