from typing import Callable

from pygame import Rect

from src.display.hud.menu.components.component import Component
from src.events.queue import EventQueue as Events
from src.sounds.sound import Sound


class Button(Component):
    
    def __init__(self, rect: Rect, on_click: Callable[[None], None], *args):
        super().__init__(rect)
        
        self.on_click = on_click
        self.args = args
        
    def update(self, dt: int):
        if self.is_hovered and Events.click:
            self.on_click(*self.args)
            Sound.play("button.click", "menu")
