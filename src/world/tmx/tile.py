from pygame import Rect, Surface, Vector2
from pygame.sprite import Sprite


class Tile(Sprite):
    
    def __init__(self, pos: Vector2, surface: Surface):
        super().__init__()

        self.image = surface
        self.rect = Rect(*pos, *surface.get_size())
