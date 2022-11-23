from src.display.resource import Resource
from src.display.window import Window
from src.utils.consts import COLOR_BTN_TEXT


class Debug:
    
    class Infos:
        fps: int

    @classmethod
    def init(cls):
        cls.visible = False
        cls._font = Resource.fnt("main24")

    @classmethod
    def render(cls):
        
        text_surface = cls._font.render(f"FPS : {cls.Infos.fps}", True, COLOR_BTN_TEXT)
        Window.hud_surface.blit(
            text_surface,
            text_surface.get_rect(topleft=(10, 10)),
        )
