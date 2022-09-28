from src.display.hud.menu.menu import Menu
from src.display.hud.menu.components.button import Button

from src.lang import Lang


class LangMenu(Menu):
    
    @classmethod
    def init(cls):
        cls.components = (
            Button("lang.fr",   (540, 250, 200, 50), Lang.load, (Lang.Langs.FR,)),
            Button("lang.en",   (540, 310, 200, 50), Lang.load, (Lang.Langs.EN,)),

            Button("menu.back", (540, 430, 200, 50), cls.close),
        )
