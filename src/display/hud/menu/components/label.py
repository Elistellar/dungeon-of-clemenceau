from pygame import Rect

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.settings.lang import Lang
from src.utils.consts import COLOR_BUTTON_TEXT


class Label(Component):
    
    X_SHIFT = 12
    
    def __init__(self, rect: Rect, text: str):
        super().__init__(rect)

        self.text = text
        
    def render(self):
        text_surface = self.FONT.render(Lang[self.text], True, COLOR_BUTTON_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(bottom=self.rect.top, left=self.rect.left + self.X_SHIFT)
        )
