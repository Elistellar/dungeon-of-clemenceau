from typing import List

from pygame import Rect

from src.display.window import Window
from src.display.resource import Resource
from src.utils.consts import COLOR_BUTTON_TEXT
from src.sounds.sound import Sound
from src.settings.lang import Lang


class Notification:
    
    WIDTH = 256
    HEIGHT = 64
    MARGIN = 12
    ANIMATION_SPEED = 0.2
    
    __queue: List["Notification"] = []
    
    @classmethod
    def init(cls):
        cls.TOPLEFT = Window.hud_surface.get_width()
        cls.SURFACE = Resource.img("menu.large_button")
        cls.FONT = Resource.fnt("main24")
    
    @classmethod
    def update(cls, dt: int):
        for i, notif in enumerate(cls.__queue):
            notif.time_visible += dt
            
            if notif.time_visible > notif.duration:
                cls.__queue.remove(notif)
                del notif
            else:
                notif.rect.x = max(
                    cls.TOPLEFT - cls.WIDTH - cls.MARGIN,
                    notif.rect.x - dt * cls.ANIMATION_SPEED
                )
    
                notif.rect.y = cls.MARGIN + i * (cls.MARGIN + cls.HEIGHT)
    
    @classmethod
    def render(cls):
        for notif in cls.__queue:
            
            Window.hud_surface.blit(
                cls.SURFACE,
                notif.rect
            )
            
            Window.hud_surface.blit(
                notif.icon,
                notif.rect
            )
            
            Window.hud_surface.blit(
                notif.text_surface,
                notif.text_surface.get_rect(
                    x=notif.rect.x + cls.HEIGHT + cls.MARGIN,
                    centery=notif.rect.centery
                )
            )

    def __init__(self, icon_name: str, title: str, duration: int):
        """
        Show a notification on the hud.
        
        Args:
            duration: duration notification will be visible (in seconds)
        """
        Notification.__queue.append(self)
        Sound.play("menu.notif", "menu")
        
        self.title = title
        self.duration = duration * 1000
        self.time_visible = 0
        
        self.icon = Resource.img(f"icon.{icon_name}")
        self.rect = Rect(self.TOPLEFT, self.MARGIN, self.WIDTH, self.HEIGHT)
        self.text_surface = self.FONT.render(Lang[self.title], True, COLOR_BUTTON_TEXT)
