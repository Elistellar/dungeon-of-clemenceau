from typing import Callable, Tuple

from pygame import Rect
from pygame.draw import rect as draw_rect

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.lang import Lang
from src.sound import Sound
from src.utils.consts import COLOR_BTN_BG, COLOR_BTN_BG_HOVER, COLOR_BTN_TEXT


class Button(Component):
    """
    A button component for menus
    """
    
    def __init__(self, text: str, rect: Tuple[int, int, int, int], on_click: Callable[..., None], args = tuple()):
        """
        Create a new Button.
        
        Parameters:
            text (str): The text code to be written on the button
            rect (Tuple[int, int, int, int]): The position and size of the button (x, y, width, height)
            on_click (Callable[..., None]): A function which will be called when the button is clicked
            args (tuple): The arguments to pass to the previous function on call        
        """
        self.rect = Rect(*rect)
        self.text = text
        self.on_click = on_click
        self.args = args
        
        self.is_hovered = False
        
    def update(self):
        # Hovering
        if self.rect.collidepoint(self.mouse_pos):
            if not self.is_hovered:
                Sound.play("btn_hover", "menu")
                self.is_hovered = True
            
            # Click
            if self.left_click:
                Sound.play("btn_click", "menu")
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
