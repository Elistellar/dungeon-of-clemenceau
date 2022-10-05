from pygame import Rect
from pygame.sprite import Sprite


class Obstacle(Sprite):
    """
    A sprite that only have an hitbox.
    """
    
    def __init__(self, rect: Rect):
        """
        Create a new obstacle.
        """
        super().__init__()
        self.rect = rect
