from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.small_button import SmallButton
from src.settings.lang import Lang


class LanguageMenu(BaseMenu):
    
    @classmethod
    def init(cls):
        cls.components = (
            (SmallButton((570, 252), "fr", Lang.load, Lang.Langs.FR), SmallButton((646, 252), "en", Lang.load, Lang.Langs.EN)),
            (LargeButton((512, 404), "menu.back", cls.back), None)
        )
