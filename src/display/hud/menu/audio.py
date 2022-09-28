from src.display.hud.menu.menu import Menu
from src.display.hud.menu.components.button import Button


class AudioMenu(Menu):
    
    @classmethod
    def init(cls):
        cls.components = (
            Button("menu.back",     (540, 430, 200, 50), cls.close),
        )
