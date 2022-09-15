from pygame import Surface, Rect
from pygame.sprite import Sprite

from src.display.camera import Camera


class Tile(Sprite):
    
    def __init__(self, surface: Surface, rect: Rect):
        super().__init__(Camera)
        
        self.image = surface
        self.rect = rect
