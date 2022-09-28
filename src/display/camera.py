from pygame.math import Vector2
from pygame.sprite import Group

from src.display.window import Window
from src.utils.hinting import HasRect


class _Camera(Group):
    
    @classmethod
    def init(cls):
        cls.screen_center = Vector2(Window.surface.get_size()) * 0.5
        
        cls.offset = Vector2()
        cls.background = Group()
            
    def draw(self, center: HasRect):

        blit = Window.surface.blit

        self.offset = Vector2(center.rect.center) - self.screen_center
        
        for sprite in self.background.sprites() + sorted(self.sprites(), key=lambda s: s.rect.centery):
                        
            blit(
                sprite.image,
                sprite.rect.topleft - self.offset
            )
            
    def empty(self):
        self.background.empty()
        super().empty()

Camera = _Camera()
