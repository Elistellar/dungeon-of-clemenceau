from src.display.hud.menu.components.button import Button
from src.display.hud.menu.menu import Menu


class KeybindsMenu(Menu):
    
    @classmethod
    def init(cls):
        cls.components = (
            Button("menu.back",     (540, 430, 200, 50), cls.close),
        )
