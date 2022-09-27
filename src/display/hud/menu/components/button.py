from typing import Callable

from pygame import Rect

from src.display.hud.menu.components.component import Component


class Button(Component):
    
    def __init__(self, text: str, rect: tuple[int, int, int, int], on_click: Callable):
        self.rect = Rect(*rect)
        self.text = text
        self.on_click = on_click
        
        self.is_hovered = False
        
    def update(self):
        if self.rect.collidepoint(self.mouse_pos):
            self.is_hovered = True
            
            if self.left_click:
                self.on_click()
        else:
            self.is_hovered = False
            
    def render(self):
        pass