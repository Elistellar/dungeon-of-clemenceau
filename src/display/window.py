from enum import Enum

from pygame import Surface
from pygame.display import flip, set_caption
from pygame.display import set_mode as open_window
from pygame.display import toggle_fullscreen
from pygame.locals import SRCALPHA
from pygame.math import Vector2
from pygame.transform import scale


class Window:
    
    ZOOM = 1.8
    
    class Size(Enum):
        FULL_HD = 1980, 1080
        HD      = 1280, 720
        HD_W    = 1280, 657
    
    @classmethod
    def init(cls, draw_size: Size, win_size: Size):
        cls.resize(win_size)
        
        cls.surface = Surface(draw_size.value)
        cls.hud_surface = Surface(draw_size.value, SRCALPHA)
        
        cls.blit = classmethod(cls.surface.blit)
        
    @classmethod
    def set_title(cls, title: str):
        set_caption(title)
        
    @classmethod
    def resize(cls, size: Size):
        cls.__screen = open_window(size.value)
        
        cls.size = size
        
        cls.__draw_size = Vector2(size.value) * cls.ZOOM
        win_size_vec = Vector2(size.value)
        top_left_pos = (cls.__draw_size - win_size_vec) // 2
        cls.__clipping = *top_left_pos, *(top_left_pos + win_size_vec)
                
    @classmethod
    def toggle_fullscreen(cls):
        """
        Switch between fullscreen and window mode. 
        """
        toggle_fullscreen()
    
    @classmethod
    def render(cls):
        
        cls.__screen.blit(
            scale(cls.surface, cls.__draw_size),
            (0, 0),
            cls.__clipping
        )
        
        cls.__screen.blit(
            scale(cls.hud_surface, cls.size.value),
            (0, 0)
        )
        
        flip()
