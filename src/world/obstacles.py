from pygame import Rect
from pygame.sprite import Sprite

from src.physics.body import Body
from src.data_storage.data_storage import DataStorage


class Obstacle(Sprite, Body):
    """
    A sprite that only have an hitbox.
    """
    
    def __init__(self, rect: Rect):
        """
        Create a new obstacle.
        """
        Sprite.__init__(self, DataStorage.obstacles)
        Body.__init__(self, rect)
