from typing import Callable

from pygame import Rect
from pygame.draw import rect as draw_rect
from pygame.key import name as get_key_name

from src.display.hud.menu.components.component import Component
from src.display.mouse import Mouse
from src.display.window import Window
from src.lang import Lang
from src.sound import Sound
from src.utils.consts import COLOR_BTN_BG, COLOR_BTN_BG_HOVER, COLOR_BTN_TEXT


class KeyInput(Component):
    
    def __init__(self, text: str, rect: tuple[int, int, int, int], setter: Callable[[int], None], getter: Callable[[], int]):
        self.rect = Rect(*rect)
        
        self.is_hovered = False
        self._waiting_for_key = False
        self.setter = setter
        self.getter = getter
        
        self.text = text
        
    def update(self):
        
        if self._waiting_for_key and self.waiting_for_key:
            if self.keyup:
                self.setter(self.keyup)
                Mouse.activate()
                self._waiting_for_key = False
                self.waiting_for_key = False
        
        elif self._waiting_for_key and not self.waiting_for_key:
            self._waiting_for_key = False
        
        else:
            if self.rect.collidepoint(self.mouse_pos):
                if not self.is_hovered:
                    Sound.play("btn_hover", "menu")
                    self.is_hovered = True
                
                if self.left_click:
                    Sound.play("btn_click", "menu")
                    Mouse.disable()
                    self._waiting_for_key = True
                    self.waiting_for_key = True
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
        
        # Label
        text_surface = self.font.render(Lang[self.text], True, COLOR_BTN_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(centerx=self.rect.centerx + 5, bottom=self.rect.top - 2)
        )
        
        # Key name
        text_surface = self.font.render(
            Lang[get_key_name(self.getter())],
            True,
            COLOR_BTN_TEXT
        )
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(center=self.rect.center),
        )
