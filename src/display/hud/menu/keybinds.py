from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton


class KeybindsMenu(BaseMenu):
    
    @classmethod
    def init(cls):
        cls.components = (
            (LargeButton((512, 404), "menu.back", cls.back),),
        )
