from typing import Callable, Tuple

from pygame import Rect

from src.display.hud.menu.components.button import Button
from src.display.window import Window
from src.settings.lang import Lang
from src.utils.consts import COLOR_BUTTON_TEXT


class LargeButton(Button):
    
    WIDTH = 256
    HEIGHT = 64
        
    def __init__(self, pos: Tuple[int, int], text: str, on_click: Callable[[None], None], *args):
        super().__init__(Rect(*pos, self.WIDTH, self.HEIGHT), on_click, *args)
        
        self.text = text
        
    def render(self):
        
        if self.is_hovered:
            Window.hud_surface.blit(
                self.LARGE_BUTTON_HOVERED,
                self.rect
            )
        else:
            Window.hud_surface.blit(
                self.LARGE_BUTTON,
                self.rect
            )
        
        text_surface = self.FONT.render(Lang[self.text], True, COLOR_BUTTON_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(center=self.rect.center)
        )
