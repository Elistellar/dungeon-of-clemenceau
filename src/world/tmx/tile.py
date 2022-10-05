from pygame import Rect, Surface, Vector2
from pygame.sprite import Sprite


class Tile(Sprite):
    """
    Represeent a tmx tile.
    """
    
    def __init__(self, pos: Vector2, surface: Surface):
        """
        Create a new tmx Tile.
        """
        super().__init__()

        self.image = surface
        self.rect = Rect(*pos, *surface.get_size())
