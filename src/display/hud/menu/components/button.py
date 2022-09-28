from typing import Callable

from pygame import Rect
from pygame.draw import rect as draw_rect

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.lang import Lang
from src.utils.consts import COLOR_BTN_BG, COLOR_BTN_BG_HOVER, COLOR_BTN_TEXT


class Button(Component):
    
    def __init__(self, text: str, rect: tuple[int, int, int, int], on_click: Callable, args = tuple()):
        self.rect = Rect(*rect)
        self.text = text
        self.on_click = on_click
        self.args = args
        
        self.is_hovered = False
        
    def update(self):
        if self.rect.collidepoint(self.mouse_pos):
            self.is_hovered = True
            
            if self.left_click:
                self.on_click(*self.args)
        else:
            self.is_hovered = False
            
    def render(self):
        
        # Background
        if self.is_hovered:
            color = COLOR_BTN_BG_HOVER
        else:
            color = COLOR_BTN_BG
        
        draw_rect(
            Window.hud_surface,
            color,
            self.rect
        )
        
        # Text
        text_surface = self.font.render(Lang[self.text], True, COLOR_BTN_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(center=self.rect.center),
        )
