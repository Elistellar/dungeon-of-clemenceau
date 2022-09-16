from pygame.math import Vector2
from pygame.sprite import Group

from src.utils.hinting import HasRect
from src.display.window import Window


class _Camera(Group):
    
    @classmethod
    def init(cls):
        cls.screen_center = Vector2(Window.surface.get_size()) * 0.5
        
        cls.offset = Vector2()
        cls.background = Group()
            
    def draw(self, center: HasRect):

        display_surface = Window.surface

        self.offset = Vector2(center.rect.center) - self.screen_center
        
        for sprite in self.background.sprites() + sorted(self.sprites(), key=lambda s: s.rect.centery):
                        
            display_surface.blit(
                sprite.image,
                sprite.rect.topleft - self.offset
            )
            
    def empty(self):
        self.background.empty()
        super().empty()

Camera = _Camera()
