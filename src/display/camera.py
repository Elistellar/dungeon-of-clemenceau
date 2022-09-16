from pygame.display import get_surface as get_screen
from pygame.math import Vector2
from pygame.sprite import Group

from src.utils.hinting import HasRect


class _Camera(Group):
    
    @classmethod
    def init(cls):        
        cls.display_surface = get_screen()
        cls.screen_center = Vector2(cls.display_surface.get_size()) * 0.5
        
        cls.offset = Vector2()
        cls.background = Group()
            
    def draw(self, center: HasRect):

        self.offset = Vector2(center.rect.center) - self.screen_center
        
        for sprite in self.background.sprites() + sorted(self.sprites(), key=lambda s: s.rect.centery):
                        
            self.display_surface.blit(
                sprite.image,
                sprite.rect.topleft - self.offset
            )
            
    def empty(self):
        self.background.empty()
        super().empty()

Camera = _Camera()
