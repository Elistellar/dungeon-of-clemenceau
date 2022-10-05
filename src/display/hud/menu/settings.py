from src.display.hud.menu.audio import AudioMenu
from src.display.hud.menu.components.button import Button
from src.display.hud.menu.keybinds import KeybindsMenu
from src.display.hud.menu.lang import LangMenu
from src.display.hud.menu.menu import Menu


class SettingsMenu(Menu):
    """
    The 'Settings' menu
    """
    
    submenus = {
        "keybinds": KeybindsMenu,
        "audio": AudioMenu,
        "lang": LangMenu,
    }
    
    @classmethod
    def init(cls):
        cls.components = (
            Button("menu.keybinds", (540, 250, 200, 50), cls.open_sub, ("keybinds",)),
            Button("menu.audio",    (540, 310, 200, 50), cls.open_sub, ("audio",)),
            Button("menu.lang",     (540, 370, 200, 50), cls.open_sub, ("lang",)),
            Button("menu.back",     (540, 430, 200, 50), cls.close),
        )
