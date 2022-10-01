from typing import Callable

from pygame import Rect
from pygame.draw import rect as draw_rect
from src.display.hud.menu.components.component import Component
from src.display.mouse import Mouse
from src.display.window import Window
from src.lang import Lang
from src.sound import Sound
from src.utils.consts import (COLOR_BTN_BG, COLOR_BTN_BG_HOVER, COLOR_BTN_TEXT,
                              COLOR_CURSOR)


class Slider(Component):
    
    def __init__(self, text: str, rect: tuple[int, int, int, int], min: int, max: int, setter: Callable[[int], None], init_value: int):
        self.rect = Rect(*rect)
        self.text = text
        
        self.cursor = self.rect.copy().inflate(0, -10)
        self.cursor.width = 5
        self.cursor.centerx = self.rect.width * (init_value - min) / (max - min) + self.rect.x
        
        self.is_hovered = False
        
        self.min = min
        self.max = max
        self.setter = setter
        
    def update(self):
        if self.rect.collidepoint(self.mouse_pos):
            if not self.is_hovered:
                Sound.play("btn_hover", "menu")
                self.is_hovered = True
            
            if self.left_click:
                Sound.play("btn_click", "menu")
                
            if self.left_click_hold:
                x = Mouse.get_pos()[0]
                self.cursor.centerx = x
                
                self.setter(
                    int((x - self.rect.x) * (self.max - self.min) / self.rect.width + self.min)
                )
                
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
        
        # Cursor
        draw_rect(
            Window.hud_surface,
            COLOR_CURSOR,
            self.cursor
        )
        
        # Label
        text_surface = self.font.render(Lang[self.text], True, COLOR_BTN_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(centerx=self.rect.centerx + 5, bottom=self.rect.top - 2)
        )
    