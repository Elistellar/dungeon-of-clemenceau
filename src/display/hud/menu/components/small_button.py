from typing import Callable, Tuple

from pygame import Rect

from src.display.hud.menu.components.button import Button
from src.display.resource import Resource
from src.display.window import Window


class SmallButton(Button):
    
    WIDTH = 64
    HEIGHT = 64
    
    def __init__(self, pos: Tuple[int, int], icon_name: str, on_click: Callable[[None], None], *args):
        super().__init__(Rect(*pos, self.WIDTH, self.HEIGHT), on_click, *args)
        
        self.icon_surface = Resource.img("icon." + icon_name)
        
    def render(self):
        
        if self.is_hovered:
            Window.hud_surface.blit(
                self.SMALL_BUTTON_HOVERED,
                self.rect
            )
        else:
            Window.hud_surface.blit(
                self.SMALL_BUTTON,
                self.rect
            )
            
        Window.hud_surface.blit(
            self.icon_surface,
            self.rect
        )
