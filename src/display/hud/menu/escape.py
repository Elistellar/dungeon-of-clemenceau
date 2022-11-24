from typing import Callable, NoReturn
from webbrowser import open as open_url

from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.small_button import SmallButton
from src.display.hud.menu.achievements import AchievementsMenu
from src.display.hud.menu.settings import SettingsMenu
from src.display.hud.menu.language import LanguageMenu


class EscapeMenu(BaseMenu):
    
    quit: Callable[[None], NoReturn] 
    
    submenus = {
        "achievements": AchievementsMenu(),
        "settings": SettingsMenu(),
        "language": LanguageMenu(),
    }
    
    @classmethod
    def init(cls):
        cls.components = (
            (LargeButton((474, 252), "menu.quit", quit), SmallButton((742, 252), "achievement", cls.open_sub, "achievements")),
            (SmallButton((474, 328), "about", cls.about), LargeButton((550, 328), "menu.settings", cls.open_sub, "settings")),
            (LargeButton((474, 404), "menu.resume", cls.escape), SmallButton((742, 404), "language", cls.open_sub, "language")),
        )
        
    @classmethod
    def about(cls):
        open_url("https://github.com/Elistellar/dungeon-of-clemenceau")
