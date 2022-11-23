from typing import Callable, NoReturn
from webbrowser import open as open_url

from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.small_button import SmallButton
from src.display.hud.menu.achievements import AchievementsMenu
from src.display.hud.menu.options import OptionsMenu
from src.display.hud.menu.language import LanguageMenu


class EscapeMenu(BaseMenu):
    
    quit: Callable[[None], NoReturn] 
    
    submenus = {
        "achievements": AchievementsMenu(),
        "option": OptionsMenu(),
        "language": LanguageMenu(),
        
    }
    
    @classmethod
    def init(cls):
        cls.components = (
            (LargeButton((0, 0), "menu.quit", quit), SmallButton((0, 0), "achievement", cls.open_sub, "achievements")),
            (SmallButton((0, 0), "about", cls.about), LargeButton((0, 0), "menu.options", cls.open_sub, "options")),
            (LargeButton((0, 0), "menu.resume", cls.escape), SmallButton((0, 0), "language", cls.open_sub, "language")),
        )
        
    @classmethod
    def about(cls):
        open_url("https://github.com/Elistellar/dungeon-of-clemenceau")
