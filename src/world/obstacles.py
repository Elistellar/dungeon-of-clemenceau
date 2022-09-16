from pygame import Rect
from pygame.sprite import Group, Sprite


class Obstacle(Sprite):
    
    def __init__(self, rect: Rect):
        super().__init__()
        self.rect = rect


Obstacles = Group()