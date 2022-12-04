from typing import Tuple

from pygame import Rect
from pygame.key import name as key_name

from src.display.hud.menu.components.component import Component
from src.display.hud.menu.components.label import Label
from src.events.queue import EventQueue as Events
from src.sounds.sound import Sound
from src.settings.settings import Settings
from src.display.window import Window
from src.utils.consts import COLOR_BUTTON_TEXT
from src.settings.lang import Lang


class KeyInput(Component):
    
    WIDTH = 128
    HEIGHT = 64
    
    def __init__(self, pos: Tuple[int, int], label: str, key: str):
        super().__init__(Rect(*pos, self.WIDTH, self.HEIGHT))
        
        self.label = Label(self.rect, label)
        self.key = key
        self.listening = False
        
    def update(self, dt: int):
        if self.is_hovered and Events.click:
            Sound.play("button.click", "menu")
            self.listening = True
            Events.listen_for_key()
        
        if self.listening and Events.key_input is not None:
            Settings.set(f"key.{self.key}", Events.key_input)
            self.listening = False
            Events.stop_listening()
            
    def render(self):
        self.label.render()
        
        if self.is_hovered:
            Window.hud_surface.blit(
                self.MEDIUM_BUTTON_HOVERED,
                self.rect
            )
        else:
            Window.hud_surface.blit(
                self.MEDIUM_BUTTON,
                self.rect
            )
        
        key_text = key_name(Settings[f"key.{self.key}"])
        if key_text not in "abcdefghijklmnopqrstuvwxyz":
            key_text = Lang["key." + key_text.replace(" ", "_")]
        else:
            key_text.upper()
        
        text_surface = self.FONT.render(
            key_text,
            True, COLOR_BUTTON_TEXT
        )
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(center=self.rect.center)
        )
