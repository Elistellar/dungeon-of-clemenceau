from pygame.display import set_caption
from pygame.display import set_mode as create_window
from pygame.display import flip
from pygame.transform import scale


class Window:
    
    SIZE = 1280, 720
    TITLE = "Dungeon Of Clemenceau"
    
    ZOOM = 1.8
    ZOOMED_SIZE = SIZE[0] * ZOOM, SIZE[1] * ZOOM
    
    TOP_LEFT = (ZOOMED_SIZE[0] - SIZE[0]) // 2, (ZOOMED_SIZE[1] - SIZE[1]) // 2
    CENTER_RECT = *TOP_LEFT, TOP_LEFT[0] + SIZE[0], TOP_LEFT[1] + SIZE[1]
    
    @classmethod
    def create(cls):
        cls._surface = create_window(cls.SIZE)
        cls.surface = cls._surface.copy()
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
        flip()