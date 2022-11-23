from pygame.math import Vector2
from pygame.sprite import Group

from src.display.window import Window
from src.utils.hinting import HasRect


class _Camera(Group):
    """
    The group used to render all sprites on screen, except hud.
    Render the background first, then all sprites from lowest 'y' to highest.
    """
    
    @classmethod
    def init(cls):
        cls.screen_center = Vector2(Window.surface.get_size()) * 0.5
        
        cls.offset = Vector2()
        cls.background = Group()
            
    def draw(self, center: HasRect):
        """
        Render all game sprites, centered on the 'center' passed.
        """

        blit = Window.surface.blit

        self.offset = Vector2(center.rect.center) - self.screen_center
        
        for sprite in self.background.sprites() + sorted(self.sprites(), key=lambda s: s.rect.centery):
            blit(
                sprite.image,
                sprite.rect.topleft - self.offset
            )
            
    def empty(self):
        """
        Clear all sprites in the camera/
        """
        self.background.empty()
        super().empty()

Camera = _Camera()
