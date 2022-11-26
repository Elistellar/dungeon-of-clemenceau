from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.small_button import SmallButton
from src.display.hud.menu.controller import ControllerMenu
from src.display.hud.menu.keybinds import KeybindsMenu
from src.display.hud.menu.language import LanguageMenu
from src.display.hud.menu.sound import SoundMenu
from src.display.hud.menu.display import DisplayMenu


class SettingsMenu(BaseMenu):
    
    submenus = {
        "keybinds": KeybindsMenu(),
        "controller": ControllerMenu(),
        "sound": SoundMenu(),
        "language": LanguageMenu(),
        "display": DisplayMenu(),
    }
    
    @classmethod
    def init(cls):
        cls.components = (
            (LargeButton((474, 252), "menu.keybinds", cls.open_sub, "keybinds"), SmallButton((742, 252), "controller", cls.open_sub, "controller")),
            (SmallButton((474, 328), "sound", cls.open_sub, "sound"),            LargeButton((550, 328), "menu.display", cls.open_sub, "display")),
            (LargeButton((474, 404), "menu.back", cls.back),                     SmallButton((742, 404), "language", cls.open_sub, "language")),
        )
