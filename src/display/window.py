from pygame import Surface
from pygame.display import flip, set_caption
from pygame.display import set_mode as create_window
from pygame.locals import SRCALPHA
from pygame.transform import scale

from src.utils.consts import WINDOW_SIZE


class Window:
    
    TITLE = "Dungeon Of Clemenceau"
    
    ZOOM = 1.8
    ZOOMED_SIZE = WINDOW_SIZE[0] * ZOOM, WINDOW_SIZE[1] * ZOOM
    
    TOP_LEFT = (ZOOMED_SIZE[0] - WINDOW_SIZE[0]) // 2, (ZOOMED_SIZE[1] - WINDOW_SIZE[1]) // 2
    CENTER_RECT = *TOP_LEFT, TOP_LEFT[0] + WINDOW_SIZE[0], TOP_LEFT[1] + WINDOW_SIZE[1]
    
    @classmethod
    def create(cls):
        cls._surface = create_window(WINDOW_SIZE)
        cls.surface = cls._surface.copy()
        cls.clean_hud_surface = Surface(cls._surface.get_size(), SRCALPHA)
        cls.hud_surface = cls.clean_hud_surface.copy()
        set_caption(cls.TITLE)

    @classmethod
    def render(cls):
        cls._surface.blit(
            scale(
                cls.surface,
                cls.ZOOMED_SIZE
            ),
            (0, 0),
            cls.CENTER_RECT
        )
        cls._surface.blit(
            cls.hud_surface,
            (0, 0)
        )
        cls.hud_surface = cls.clean_hud_surface.copy()
        flip()
