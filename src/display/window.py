from pygame.display import set_mode as create_window
from pygame.display import set_caption


class Window:
    
    SIZE = 1280, 720
    TITLE = "Dungeon Of Clemenceau"
    
    @classmethod
    def create(cls):
        cls.surface = create_window(cls.SIZE)
        set_caption(cls.TITLE)
