from typing import Callable, Tuple

from pygame import Rect

from src.display.hud.menu.components.component import Component
from src.display.hud.menu.components.label import Label
from src.display.window import Window
from src.events.queue import EventQueue as Events
from src.sounds.sound import Sound
from src.utils.functions import _map


class Slider(Component):
    
    WIDTH = 256
    HEIGHT = 64
    
    PADDINGX = 36
    
    def __init__(self, pos: Tuple[int, int], label: str, getter: Callable[[None], float], setter: Callable[[float], None], _min: float, _max: float):
        super().__init__(Rect(*pos, self.WIDTH, self.HEIGHT))
        
        self.label = Label(self.rect, label)
        self.setter = setter
        self.getter = getter
        self.min = _min
        self.max = _max
        self.cursor_rect = self.SLIDER_CURSOR.get_rect(
            centery=self.rect.centery,
            centerx=self.value_to_pos()
        )
        
    def pos_to_value(self) -> float:
        return round(_map(
            self.cursor_rect.centerx,
            self.rect.left + self.PADDINGX, self.rect.right - self.PADDINGX,
            self.min, self.max
        ), 2)
    
    def value_to_pos(self) -> float:
        return _map(
            self.getter(),
            self.min, self.max,
            self.rect.left + self.PADDINGX, self.rect.right - self.PADDINGX
        )
        
    def update(self, dt: int):
        if self.is_hovered and Events.click_pressed:
            if Events.click:
                Sound.play("button.click", "menu")
                
            self.cursor_rect.centerx = min(max(self.rect.left + self.PADDINGX, Events.cursor.x), self.rect.right - self.PADDINGX)
            self.setter(self.pos_to_value())
    
    def render(self):
        self.label.render()
        
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
            
        Window.hud_surface.blit(
            self.SLIDER_BAR,
            self.rect
        )
        
        Window.hud_surface.blit(
            self.SLIDER_CURSOR,
            self.cursor_rect
        )
